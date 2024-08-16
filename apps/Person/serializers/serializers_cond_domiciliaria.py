from rest_framework import serializers

from ..models.models_cond_domiciliaria import CondicionDomiciliaria

class CondicionDomiciliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicionDomiciliaria
        fields = '__all__'