from django.db import models


class TipoZona(models.Model):
    codigo = models.CharField(max_length=100, blank=False, null=False)
    denominacion = models.CharField(max_length=120, blank=False, null=False)
    def __str__(self):
        return self.denominacion