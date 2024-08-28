from rest_framework import serializers

from ..models.models_compra_alim import CompraAlimento

class CompraAlimentoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraAlimento
        fields = [
            'id',
            'lote', 
            'cantidad_producto',
            'total_peso',
            'costo_total',
            'precio_kilo'
            ]
    def get_precio_kilo(self, obj):
        return obj.costo_total / obj.total_peso