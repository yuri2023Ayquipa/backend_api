from django.db import models

from apps.Person.Region.departamentos.models import Departamento


class Provincia(models.Model):
    provincia = models.CharField(max_length=150, blank=False, null=False)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, blank=False, null=False)
    def __str__(self):
        return self.provincia
