from django.db import models

from apps.Person.persona.person.models import Persona
from apps.Person.personaJuridica.origen_entidad.models import OrigenEntidad

class PersonaJuridica(models.Model):
    class Meta:
        verbose_name = 'Persona Jurídica'
        verbose_name_plural = 'Personas Jurídicas'
    
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, blank=False, null=False)
    id_origen_entidad = models.ForeignKey(OrigenEntidad, on_delete=models.CASCADE, blank=False, null=False)
    razon_social = models.CharField(max_length=100, blank=False, null=False)
    nombre_comercial = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.razon_social