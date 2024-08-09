from rest_framework import serializers

from .models import TipoContribuyente

class TipoContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContribuyente
        fields = '__all__'