from django.db import models

from .models_alimentacion_diaria import Alimentacion

class DetalleAlimentacion(models.Model):
    class Meta:
        verbose_name = 'Detalle Alimentacion'
        verbose_name_plural = 'Detalles Alimentaciones'
    
    id_alimentacion = models.ForeignKey(Alimentacion, on_delete=models.PROTECT, null=False)
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)