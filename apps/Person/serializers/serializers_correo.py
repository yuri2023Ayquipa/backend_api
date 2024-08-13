from rest_framework import serializers

from ..models.models_correo import Correo

class CorreoPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = '__all__'

class CorreoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ['id_persona', 'email', 'is_primary', 'id_estado']