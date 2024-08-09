from rest_framework import serializers

from .models import Telefono


class TelefonoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = '__all__'

class TelefonoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ['id', 'id_persona', 'telefono', 'id_operador', 'tipo_telefono', 'id_estado']