from django.db import models

class Operador(models.Model):
    operador = models.CharField(max_length=50,blank=True, null=False)

    def __str__(self):
        return self.operador
