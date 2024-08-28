from django.db import models

from .models_corral import Corral
from apps.AlimentoPro.models.models_compra_alim import CompraAlimento
from apps.Person.models.models_estado import Estado

class Alimentacion(models.Model):
    class Meta:
        """Meta definition for Alimentacion."""

        verbose_name = 'Alimentacion'
        verbose_name_plural = 'Alimentacions'

    id_corral = models.ForeignKey(Corral, on_delete=models.PROTECT, null=False)
    id_compra_alimento = models.ForeignKey(CompraAlimento, on_delete=models.PROTECT, null=False)
    is_activite = models.ForeignKey(Estado, on_delete=models.PROTECT, null=False)
    Peso_alimentacion = models.DecimalField(max_digits=10, decimal_places=2)
    costo_alimentacion = models.DecimalField(max_digits=30, decimal_places=20)