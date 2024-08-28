from rest_framework import serializers

from ..models.models_person import Persona
from ..models.models_tipo_documento import  TipoDocumento
from ..models.models_tipo_contribuyente import TipoContribuyente
from ..models.models_nacionalidad import Nacionalidad
from ..models.models_cond_domiciliaria import CondicionDomiciliaria 
from ..models.models_estado import Estado

from ..models.models_person_juridica import PersonaJuridica
from ..models.models_person_natural import PersonaNatural

class PersonaSerializer(serializers.ModelSerializer):
    id_tipo_documento = serializers.PrimaryKeyRelatedField(queryset=TipoDocumento.objects.all())
    id_tipo_contribuyente = serializers.PrimaryKeyRelatedField(queryset=TipoContribuyente.objects.all(), required=False, allow_null=True)
    id_nacionalidad = serializers.PrimaryKeyRelatedField(queryset=Nacionalidad.objects.all())
    id_condicionDomiciliaria = serializers.PrimaryKeyRelatedField(queryset=CondicionDomiciliaria.objects.all())
    id_estado = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Persona
        fields = [
            'id_tipo_documento',
            'numero_documento',
            'id_tipo_contribuyente',
            'id_nacionalidad',
            'id_condicionDomiciliaria',
            'created_at',
            'updated_at',
            'id_estado'
        ]

class PersonaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'id_tipo_documento': instance.id_tipo_documento.denominacion,
            'numero_documento': instance.numero_documento,
            'id_tipo_contribuyente': instance.id_tipo_contribuyente.denominacion,
            'id_nacionalidad': instance.id_nacionalidad.denominacion,
            'id_condicionDomiciliaria': instance.id_condicionDomiciliaria.denominacion,
            'id_estado': instance.id_estado.is_active
        }
    
class PersonaGetSerializer(serializers.ModelSerializer):
    tipo_documento = serializers.CharField(source='id_tipo_documento.denominacion')
    nombre_completo = serializers.SerializerMethodField()
    nombre_comercial = serializers.SerializerMethodField()

    class Meta:
        model = Persona
        fields = [
            'id',
            'tipo_documento',
            'numero_documento',
            'nombre_completo',
            'nombre_comercial',
        ]
    
    def get_nombre_completo(self, obj):
        try:
            persona_natural = obj.personanatural
            return f"{persona_natural.primer_nombre} {persona_natural.segundo_nombre or ''} {persona_natural.apellido_paterno} {persona_natural.apellido_materno}".strip()
        except PersonaNatural.DoesNotExist:
            return None

    def get_nombre_comercial(self, obj):
        try:
            persona_juridica = obj.personajuridica
            return persona_juridica.nombre_comercial
        except PersonaJuridica.DoesNotExist:
            return None

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'tipo_documento': instance.id_tipo_documento.denominacion,
            'numero_documento': instance.numero_documento,
        }

        nombre_completo = self.get_nombre_completo(instance)
        if nombre_completo:
            representation['nombre_completo'] = nombre_completo

        nombre_comercial = self.get_nombre_comercial(instance)
        if nombre_comercial:
            representation['nombre_comercial'] = nombre_comercial

        return representation