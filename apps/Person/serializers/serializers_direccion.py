from rest_framework import serializers

from ..models.models_direccion import Direccion

class DireccionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id_persona', 'ubigeo', 'id_departamento', 
                  'id_provincia', 'id_distrito', 'id_tipo_zona', 
                  'id_tipo_via', 'direccion', 'numero', 'piso', 'id_estado']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'