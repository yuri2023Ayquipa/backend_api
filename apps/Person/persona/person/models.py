from django.db import models

from apps.Person.estado.models import Estado
from apps.Person.persona.tipo_documento.models import TipoDocumento
from apps.Person.persona.tipo_contribuyente.models import TipoContribuyente
from apps.Person.persona.nacionalidad.models import Nacionalidad
from apps.Person.persona.condicion_domiciliado.models import CondicionDomiciliaria

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
    

