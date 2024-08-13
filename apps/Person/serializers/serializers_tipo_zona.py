from rest_framework import serializers
from ..models.models_tipo_zona import TipoZona

class TipoZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoZona
        fields = '__all__'

