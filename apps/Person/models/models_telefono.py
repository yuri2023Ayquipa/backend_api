from django.db import models

from .models_person import Persona
from .models_estado import Estado
from .models_operador import Operador

# Create your models here.
class Telefono(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT, blank=False, null=False)
    telefono = models.CharField(max_length=20, blank=False, null=False)
    id_operador = models.ForeignKey(Operador, on_delete=models.PROTECT, blank=False, null=False)
    id_estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=False, null=False)
    tipo_telefono = models.CharField(max_length=50, choices=[
        ('Movil', 'Móvil'),
        ('Fijo', 'Fijo'),
        ('Trabajo', 'Trabajo'),
        ('Casa', 'Casa'),
        ('Otro', 'Otro')
    ], blank=True, null=True)
    is_primary = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telefono



#is_primary:
    #BooleanField: Indica si este correo es el principal de la persona. El valor predeterminado es False.

#is_verified:
    #BooleanField: Indica si este correo ha sido verificado. El valor predeterminado es False.
#verified_at:
    #DateTimeField: Almacena la fecha y hora en que se verificó el correo. Puede ser null y estar en blanco (blank=True).

#created_at:
    #DateTimeField: Almacena la fecha y hora en que se creó el registro. Se establece automáticamente al crear el objeto (auto_now_add=True).

#updated_at:
    #DateTimeField: Almacena la fecha y hora en que se actualizó por última vez el registro. Se actualiza automáticamente cada vez que se guarda el objeto (auto_now=True).