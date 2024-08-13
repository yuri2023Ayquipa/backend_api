from django.db import models

from .models_person import Persona
from .models_estado import Estado

class Correo(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    is_primary = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.correo



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