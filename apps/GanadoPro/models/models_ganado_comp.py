from django.db import models

from apps.Person.models.models_proveedor import Proveedor

class GanadoCompra(models.Model):
    class Meta:
        verbose_name = 'Compra de Ganado'
        verbose_name_plural = 'Compras de Ganado'

    lote = models.CharField(max_length=5, null=False)
    cantidad = models.IntegerField(null=False)
    costo_total = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    fecha_compra = models.DateField(auto_now_add=True, null=False)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, null=False)