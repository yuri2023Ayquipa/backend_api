from rest_framework import serializers

from .models import PersonaJuridica

class PersonaJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaJuridica
        fields = '__all__'



