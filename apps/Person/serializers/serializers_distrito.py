from rest_framework import serializers
from ..models.models_distrito import Distrito
from ..models.models_provincia import Provincia


class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = ['id', 'distrito']


class ProvinciaDetailSerializer(serializers.ModelSerializer):
    distritos = serializers.SerializerMethodField()

    class Meta:
        model = Provincia
        fields = ['id', 'provincia', 'distritos']
    
    def get_distritos(self, obj):
        distritos = Distrito.objects.filter(id_provincia=obj.id)
        return DistritoSerializer(distritos, many=True).data