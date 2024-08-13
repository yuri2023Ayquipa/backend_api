from rest_framework import serializers

from ..models.models_operador import Operador

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ['id', 'operador']