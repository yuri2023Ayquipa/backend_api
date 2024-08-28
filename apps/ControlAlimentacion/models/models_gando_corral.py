from django.db import models

from .models_corral import Corral

class GanadoCorral(models.Model):
    class Meta:
        verbose_name = 'Ganado Corral'
        verbose_name_plural = 'Ganado Corral'
    
    id_corral = models.ForeignKey(Corral, on_delete=models.PROTECT, null=False)
    lote = models.CharField(max_length=6, null=False)
    cantidad = models.IntegerField(null=False)