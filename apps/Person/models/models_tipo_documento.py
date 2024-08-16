from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
    class Meta:
        verbose_name = 'Documento'
    
    id_sunat = models.CharField(max_length=10, unique=False, blank=False, null=False)
    denominacion = models.CharField(max_length=50, unique=False, blank=False, null=False)
    
    def __str__(self):
        return self.denominacion