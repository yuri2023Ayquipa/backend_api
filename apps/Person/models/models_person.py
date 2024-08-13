from django.db import models

from .models_estado import Estado
from .models_tipo_documento import TipoDocumento
from .models_tipo_contribuyente import TipoContribuyente
from .models_nacionalidad import Nacionalidad
from .models_cond_domiciliaria import CondicionDomiciliaria

class Persona(models.Model):
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    id_tipo_documento = models.ForeignKey(TipoDocumento,on_delete=models.PROTECT, blank=False , null=False)
    numero_documento = models.CharField(max_length=20,unique=True, blank=False, null=False)
    id_tipo_contribuyente = models.ForeignKey(TipoContribuyente, on_delete=models.PROTECT, blank=True, null=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT, blank=False, null=False)
    id_condicionDomiciliaria = models.ForeignKey(CondicionDomiciliaria, on_delete=models.PROTECT, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.numero_documento
    

