from django.db import models

from .models_sexo_ganado import SexoGanado
from apps.Person.models.models_estado import Estado

class Ganado(models.Model):
    class Meta:
        verbose_name = 'Ganado'
        verbose_name_plural = 'Ganados'

    descripcion = models.CharField(max_length=250, null=False)
    raza = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    id_sexo_g = models.ForeignKey(SexoGanado, on_delete=models.PROTECT, null=False)
    color = models.CharField(max_length=250, null=False)
    marca = models.CharField(max_length=5, null=False, default="-")
    is_activite = models.ForeignKey(Estado, on_delete=models.PROTECT, null=False, default=1)