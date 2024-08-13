from rest_framework import serializers

from ..models.models_tipo_contribuyente import TipoContribuyente

class TipoContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContribuyente
        fields = '__all__'