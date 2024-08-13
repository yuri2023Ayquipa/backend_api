from django.db import models

class Departamento(models.Model):
    departamento = models.CharField(max_length=150, blank=False, null=False)
    def __str__(self):
        return self.departamento

 