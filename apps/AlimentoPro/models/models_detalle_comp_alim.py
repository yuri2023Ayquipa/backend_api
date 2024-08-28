from django.db import models

from .models_alimento import Alimentos
from .models_compra_alim import CompraAlimento
from apps.Person.models.models_proveedor import Proveedor


# Create your models here.
class DetalleCompAlimento(models.Model):
    class Meta:
        verbose_name = 'Detalle de Compra de Alimento'
        verbose_name_plural = 'Detalles de Compras de Alimentos'

    fecha_compra = models.DateField(null=False)
    id_comp_alim = models.ForeignKey(CompraAlimento, on_delete=models.PROTECT, null=False)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, null=False)
    id_alimento = models.ForeignKey(Alimentos, on_delete=models.PROTECT, null=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    peso_total = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    costo_unidad = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    costo_total = models.DecimalField(max_digits=12, decimal_places=2, null=False)