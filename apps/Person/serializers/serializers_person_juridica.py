from rest_framework import serializers

from ..models.models_person_juridica import PersonaJuridica
from ..models.models_origen_entidad import OrigenEntidad
from ..models.models_person import Persona

from .serializers_person import PersonaSerializer, PersonaListSerializer

class PersonaJuridicaGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        
    def to_representation(self, instance):
        return {
            'id_persona': PersonaListSerializer(instance.id_persona).data,
            'id': instance.id,
            'id_origen_entidad': instance.id_origen_entidad.denominacion,
            'razon_social': instance.razon_social,
            'nombre_comercial': instance.nombre_comercial
        }

class PersonaJuridicaPostSerializer(serializers.ModelSerializer):
    id_persona = PersonaSerializer()
    id_origen_entidad = serializers.PrimaryKeyRelatedField(queryset=OrigenEntidad.objects.all())
    class Meta:
        model = PersonaJuridica
        fields = [
            'id_persona',
            'id_origen_entidad',
            'razon_social',
            'nombre_comercial',
        ]

    def create(self, validated_data):
        persona_data = validated_data.pop('id_persona')
        persona = Persona.objects.create(**persona_data)
        persona_juridica = PersonaJuridica.objects.create(id_persona=persona, **validated_data)
        return persona_juridica