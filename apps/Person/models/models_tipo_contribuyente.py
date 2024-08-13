from django.db import models

class TipoContribuyente(models.Model):
    class Meta:
        verbose_name = 'Tipo Contribuyente'

    codigo = models.CharField(max_length=6, blank=False, null=False)
    denominacion = models.CharField(max_length=220, blank=False, null=False)

    def __str__(self):
        return self.denominacion