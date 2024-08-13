from rest_framework import serializers

from ..models.models_person_natural import PersonaNatural

class PersonaNaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaNatural
        fields = '__all__'

