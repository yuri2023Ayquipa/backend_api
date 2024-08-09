from rest_framework import serializers
from .models import TipoVia

class TipoViaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVia
        fields = '__all__'