from rest_framework import serializers

from ..models.models_person import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class PersonaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id','id_tipo_documento', 'numero_documento', 'id_tipo_contribuyente', 'id_nacionalidad', 'id_condicionDomiciliaria', 'id_estado']