from rest_framework import serializers

from .models import CondicionDomiciliaria

class CondicionDomiciliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicionDomiciliaria
        fields = ['id', 'codigo', 'denominacion']