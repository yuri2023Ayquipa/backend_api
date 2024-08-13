from django.db import models

from .models_departamento import Departamento
from .models_provincia import Provincia
from .models_distrito import Distrito
from .models_tipo_zona import TipoZona
from .models_tipo_via import TipoVia

from .models_person import Persona
from .models_estado import Estado

class Direccion(models.Model):
    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT, blank=True, null=True)
    ubigeo = models.CharField(max_length=10, blank=True, null=True)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, blank=False, null=False)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=False, null=False)
    id_distrito = models.ForeignKey(Distrito, on_delete=models.PROTECT, blank=False, null=False)
    id_tipo_zona = models.ForeignKey(TipoZona, on_delete=models.PROTECT, blank=True, null=True)
    id_tipo_via = models.ForeignKey(TipoVia, on_delete=models.PROTECT, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=False)
    numero = models.CharField(max_length=10, blank=True, null=True)
    piso = models.CharField(max_length=10, blank=True, null=True)
    bloque = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return f"{self.direccion}, {self.numero}, {self.piso}, {self.bloque}"



# Añadí created_at y updated_at para llevar un registro de cuándo se creó y se actualizó cada registro.