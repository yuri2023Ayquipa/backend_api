from rest_framework import serializers
from ..models.models_tipo_via import TipoVia

class TipoViaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVia
        fields = '__all__'