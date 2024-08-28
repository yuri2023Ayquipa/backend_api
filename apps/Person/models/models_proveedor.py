from django.db import models

from .models_person import Persona
from .models_estado import Estado

class Proveedor(models.Model):
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT, null=False)
    id_estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=False)