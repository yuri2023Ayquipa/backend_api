from rest_framework import serializers

from ..models.models_person_juridica import PersonaJuridica

class PersonaJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = '__all__'



