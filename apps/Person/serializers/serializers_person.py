from rest_framework import serializers

from ..models.models_person import Persona
from ..models.models_tipo_documento import  TipoDocumento
from ..models.models_tipo_contribuyente import TipoContribuyente
from ..models.models_nacionalidad import Nacionalidad
from ..models.models_cond_domiciliaria import CondicionDomiciliaria 
from ..models.models_estado import Estado

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
        fields = ['id','id_tipo_documento', 'numero_documento', 'id_tipo_contribuyente', 'id_nacionalidad', 'id_condicionDomiciliaria', 'id_estado']