from django.db import models

class TipoVia(models.Model):
    codigo = models.CharField(max_length=100, blank=False, null=False)
    deniminacion = models.CharField(max_length=150, blank=False, null=False)
    def __str__(self):
        return self.deniminacion  