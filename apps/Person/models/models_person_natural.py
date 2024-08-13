from django.db import models

from .models_person import Persona
from .models_genero import Genero

class PersonaNatural(models.Model):
    
    class Meta():
        verbose_name = 'Persona Natural'
        verbose_name_plural = 'Personas Naturales'    

    id_persona = models.OneToOneField(Persona, on_delete=models.PROTECT, blank=False, null= False)
    primer_nombre = models.CharField(max_length=50, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50, blank=False, null=False)
    apellido_materno = models.CharField(max_length=50, blank=False, null=False)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(Genero, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.primer_nombre
    