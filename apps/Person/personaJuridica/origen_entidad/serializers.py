from rest_framework import serializers

from .models import OrigenEntidad

class OrigenEntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrigenEntidad
        fields = ['id', 'codigo', 'denominacion']