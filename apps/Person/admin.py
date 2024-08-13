from django.contrib import admin

from .models.models_correo import Correo
from .models.models_operador import Operador
from .models.models_telefono import Telefono
from .models.models_direccion import Direccion
from .models.models_estado import Estado
from .models.models_cond_domiciliaria import CondicionDomiciliaria
from .models.models_nacionalidad import Nacionalidad
from .models.models_origen_entidad import OrigenEntidad
from .models.models_person import Persona
from .models.models_tipo_contribuyente import TipoContribuyente
from .models.models_tipo_documento import TipoDocumento
from .models.models_person_juridica import PersonaJuridica
from .models.models_person_natural import PersonaNatural
from .models.models_genero import Genero
from .models.models_departamento import Departamento
from .models.models_distrito import Distrito
from .models.models_provincia import Provincia
from .models.models_tipo_via import TipoVia
from .models.models_tipo_zona import TipoZona

# Register your models here.
admin.site.register(Correo)
admin.site.register(Operador)
admin.site.register(Telefono)

admin.site.register(Direccion)

admin.site.register(Estado)

admin.site.register(CondicionDomiciliaria)
admin.site.register(Nacionalidad)
admin.site.register(OrigenEntidad)
admin.site.register(Persona)
admin.site.register(TipoContribuyente)
admin.site.register(TipoDocumento)

admin.site.register(PersonaJuridica)
admin.site.register(PersonaNatural)
admin.site.register(Genero)

admin.site.register(Departamento)
admin.site.register(Distrito)
admin.site.register(Provincia)
admin.site.register(TipoVia)
admin.site.register(TipoZona)






