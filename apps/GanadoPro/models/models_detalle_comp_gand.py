from django.db import models

from .models_ganado_comp import GanadoCompra
from .models_ganado import Ganado

# Create your models here.
class DetalleCompraGanado(models.Model):
    class Meta:
        verbose_name = 'Detalle Compra Ganado'
        verbose_name_plural = 'Detalles Compra Ganado'

    id_compra = models.ForeignKey(GanadoCompra, on_delete=models.PROTECT, null=False)
    id_ganado = models.ForeignKey(Ganado, on_delete=models.PROTECT, null=False)
    precio = models.DecimalField(max_digits=30, decimal_places=20, null=False) 
