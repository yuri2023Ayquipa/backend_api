from django.contrib import admin

from .contacto.correo.models import Correo
from .contacto.operador.models import Operador
from .contacto.Telefono.models import Telefono

from .Direccion.models import Direccion

from .estado.models import Estado

from .persona.condicion_domiciliado.models import CondicionDomiciliaria
from .persona.nacionalidad.models import Nacionalidad
from .personaJuridica.origen_entidad.models import OrigenEntidad
from .persona.person.models import Persona
from .persona.tipo_contribuyente.models import TipoContribuyente
from .persona.tipo_documento.models import TipoDocumento

from .personaJuridica.models import PersonaJuridica
from .personaNatural.models import PersonaNatural
from .personaNatural.genero.models import Genero

from .Region.departamentos.models import Departamento
from .Region.distritos.models import Distrito
from .Region.provincias.models import Provincia
from .Region.tipos_vias.models import TipoVia
from .Region.tipos_zonas.models import TipoZona







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






