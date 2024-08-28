from rest_framework import serializers

from ..models.models_alimento import Alimentos

class AlimentosGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = '__all__'

class AlimentosPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = '__all__'