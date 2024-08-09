from django.urls import path

from .estado.views import * 

from .persona.person.views import PersonaView, PersonaDetailView
from .persona.tipo_contribuyente.views import * 
from .persona.tipo_documento.views import *
from .personaJuridica.origen_entidad.views import *
from .persona.nacionalidad.views import *
from .persona.condicion_domiciliado.views import *

from .contacto.correo.views import CorreoView, CorreoDetailView
from .contacto.operador.views import OperadorView
from .contacto.Telefono.views import TelefonoView, TelefonoDetalleView

from .Direccion.views import DireccionView, DireccionDetalleView

from .Region.departamentos.views import *
from .Region.provincias.views import *
from .Region.distritos.views import *
from .Region.tipos_vias.views import *
from .Region.tipos_zonas.views import *

from .personaJuridica.views import PersonaJuridicaView, PersnaJuridicaDetailView



from .personaNatural.views import PersonaNaturalView, PersonaNaturalDetailView
from .personaNatural.genero.views import GeneroView

urlpatterns = [
    path('estado/', EstadoView.as_view(), name='estado-list'),

    path('correo/', CorreoView.as_view(), name='correo-list'),
    path('correo/<str:pk>', CorreoDetailView.as_view(), name='correo-detail'),

    path('telefono/', TelefonoView.as_view(), name='telefono-list'),
    path('telefono/<str:pk>', TelefonoDetalleView.as_view(), name='telefono-detail'),

    path('operador/', OperadorView.as_view(), name='operador-list'),
    #path('operador/<str:pk>'),

    path('direccion/', DireccionView.as_view(), name='direccion-list'),
    path('direccion/<str:pk>', DireccionDetalleView.as_view(), name='direccion-detail'),


    path('persona/', PersonaView.as_view(), name='persona-list'),
    path('persona/<str:pk>', PersonaDetailView.as_view(), name='persona-detail'),

    path('tipo_documento/', TipoDocumentoView.as_view(), name='documento-list'),
    path('tipo_contribuyente/', TipoContribuyenteView.as_view(), name='contribuyente-list'),
    path('origen_entidad/', OrigenEntidadView.as_view(), name='origen-list'),
    path('nacionalidad/', NacionalidadView.as_view(), name='nacionalidad-list'),
    path('condicion_domiciliado/', CondicionDomiciliadoView.as_view(), name='condicion-list'),


    path('departamento/', DepartamentoView.as_view(), name='departamento-list'),
    path('provincia/<int:id_departamento>/', DepartamentoDetailView.as_view(), name='provincia-list'),
    path('distrito/<int:id_provincia>/', ProvinciaDetailView.as_view(), name='distrito-list'),
    path('tipo_via/', TipoViaView.as_view(), name='tipo-via-list'),
    path('tipo_zona/', TipoZonaView.as_view(), name='tipo-zona-list'),
    
    path('personaJuridica', PersonaJuridicaView.as_view(), name="perona-list"),
    path('personaJuridica/<str:pk>', PersnaJuridicaDetailView.as_view(), name="persona-detail"),

    path('personaNatural', PersonaNaturalView.as_view(), name="perona-list"),
    path('personaNatural/<str:pk>', PersonaNaturalDetailView.as_view(), name="persona-detail"),
    path('genero/', GeneroView.as_view(), name='genero-list')
]

