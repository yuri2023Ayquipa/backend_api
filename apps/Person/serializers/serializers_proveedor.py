from rest_framework import serializers

from ..models.models_proveedor import Proveedor

from .serializers_person import PersonaGetSerializer

class ProveedorGetSerializer(serializers.ModelSerializer):
    id_persona = PersonaGetSerializer()
    class Meta:
        model = Proveedor
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'id_persona': PersonaGetSerializer(instance.id_persona).data,
        }

class ProveedorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'  