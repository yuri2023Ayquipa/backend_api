from django.db import models

from .models_unidad_medida import UnidadMedida
from apps.Person.models.models_estado import Estado

# Create your models here.
class Alimentos(models.Model):
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'

    descripcion = models.CharField(max_length=250, null=False)
    marca = models.CharField(max_length=200, null=False)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    id_unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT, null=False)
    is_active = models.ForeignKey(Estado, on_delete=models.PROTECT, null=False, default=1)
