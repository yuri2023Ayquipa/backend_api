from rest_framework import serializers

from ..models.models_alimento import Alimentos
from ..models.models_compra_alim import CompraAlimento

from .serializers_compra_alim import CompraAlimentoGetSerializer

class CompraAlimentoGetSerializers(serializers.ModelSerializer):
    id_comp_alim = CompraAlimentoGetSerializer()
    class Meta:
        model = CompraAlimento
    
    def to_representation(self, instance):
        return {
            'id_comp_alim',
            'fecha_compra',
            'id_proveedor',
            'id_alimento',
            'cantidad',
            'peso_total',
            'precio_unidad',
            'costo_total'
        }