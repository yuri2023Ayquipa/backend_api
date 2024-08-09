from rest_framework import serializers
from .models import TipoZona

class TipoZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoZona
        fields = '__all__'

