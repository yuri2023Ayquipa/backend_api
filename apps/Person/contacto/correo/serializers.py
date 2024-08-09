from rest_framework import serializers

from .models import Correo

class CorreoPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = '__all__'

class CorreoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ['id_persona', 'email', 'is_primary', 'id_estado']