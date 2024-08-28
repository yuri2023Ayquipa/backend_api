from django.db import models

# Create your models here.

class Corral(models.Model):
    class Meta:
        verbose_name = 'Corral'
        verbose_name_plural = 'Corrales'
    
    nombre_c = models.CharField(max_length=50, null=False)
    