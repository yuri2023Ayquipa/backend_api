from rest_framework import serializers
from ..models.models_provincia import  Provincia
from ..models.models_departamento import Departamento

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', 'provincia']

class DepartamentoDetailSerializer(serializers.ModelSerializer):
    provincias = serializers.SerializerMethodField()

    class Meta:
        model = Departamento
        fields = ['id', 'departamento', 'provincias']

    def get_provincias(self, obj):
        provincias = Provincia.objects.filter(id_departamento=obj.id)
        return ProvinciaSerializer(provincias, many=True).data