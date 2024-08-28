from rest_framework import serializers

from ..models.models_direccion import Direccion

class DireccionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        
    def to_representation(self, instance):
        return {
            'id_persona': instance.id_persona.id,
            'ubigeo': instance.ubigeo,
            'id_departamento': instance.id_departamento.departamento,
            'id_provincia': instance.id_provincia.provincia,
            'id_distrito': instance.id_distrito.distrito,
            'id_tipo_zona': instance.id_tipo_zona.denominacion,
            'id_tipo_via': instance.id_tipo_via.deniminacion,
            'direccion': instance.direccion,
            'numero': instance.numero,
            'piso': instance.piso,
            'id_estado': instance.id_estado.is_active
        }

class DireccionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'