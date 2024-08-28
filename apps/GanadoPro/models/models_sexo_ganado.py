from django.db import models

class SexoGanado(models.Model):
    denominacion = models.CharField(max_length=15)
    abreviatura= models.CharField(max_length=1)