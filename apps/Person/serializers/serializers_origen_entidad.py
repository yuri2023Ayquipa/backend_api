from rest_framework import serializers

from ..models.models_origen_entidad import OrigenEntidad

class OrigenEntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrigenEntidad
        fields = ['id', 'codigo', 'denominacion']