from django.db import models

from apps.GanadoPro.models.models_ganado import Ganado
from .models_gando_corral import GanadoCorral
from apps.Person.models.models_estado import Estado
class DetalleGanadoCorral(models.Model):
    class Meta:
        verbose_name = 'Detalle Ganado Corral'
        verbose_name_plural = 'Detalles Ganado Corral'

    id_ganado = models.ForeignKey(Ganado, on_delete=models.PROTECT, null=False)
    id_corral = models.ForeignKey(GanadoCorral, on_delete=models.PROTECT, null=False)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_salida = models.DateField(null=True, blank=True)
    is_activite = models.ForeignKey(Estado, on_delete=models.PROTECT, default=1)
    observacion = models.CharField(max_length=250, null=True)