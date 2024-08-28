from django.db import models

# Create your models here.
class UnidadMedida(models.Model):
    class Meta:
        verbose_name = 'Unidad de Medida'
    
    denominacion = models.CharField(max_length=50, null=False)
    abreviatura = models.CharField(max_length=5, null=False)