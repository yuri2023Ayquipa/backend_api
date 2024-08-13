from django.db import models

from .models_provincia import Provincia


class Distrito (models.Model):
    distrito = models.CharField(max_length=150, blank=False, null=False)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=False, null=False)
    def __str__(self):
        return self.distrito
