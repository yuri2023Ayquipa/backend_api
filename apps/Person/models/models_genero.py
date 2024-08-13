from django.db import models

from .models_person import Persona


class Genero(models.Model):
    codigo = models.CharField(max_length=10, blank=False, null=False)
    denominacion = models.CharField(max_length=50, null=False, blank=False, unique=False)
    abreviatura = models.CharField(max_length=1, blank=False, null=False)

    def __str__(self):
        return self.abreviatura