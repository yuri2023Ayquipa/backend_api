from rest_framework import serializers

from ..models.models_nacionalidad import Nacionalidad

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = ['id', 'codigo', 'denominacion']