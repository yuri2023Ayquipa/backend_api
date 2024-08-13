from django.urls import path

from .views.views_estado import EstadoView

from .views.views_person import PersonaView, PersonaDetailView
from .views.views_tipo_contribuyente import TipoContribuyenteView 
from .views.views_tipo_documento import TipoDocumentoView
from .views.views_origen_entidad import OrigenEntidadView
from .views.views_nacionalidad import NacionalidadView
from .views.views_cond_domiciliaria import CondicionDomiciliadoView

from .views.views_correo import CorreoView, CorreoDetailView
from .views.views_operador import OperadorView
from .views.views_telefono import TelefonoView, TelefonoDetalleView

from .views.views_direccion import DireccionView, DireccionDetalleView

from .views.views_departamento import DepartamentoView
from .views.views_provincia import ProvinciaView
from .views.views_distrito import DistritoView
from .views.views_tipo_via import TipoViaView
from .views.views_tipo_zona import TipoZonaView

from .views.views_person_juridica import PersonaJuridicaView, PersnaJuridicaDetailView



from .views.views_person_natural import PersonaNaturalView, PersonaNaturalDetailView
from .views.views_genero import GeneroView

urlpatterns = [
    path('estado/', EstadoView.as_view(), name='estado-list'),

    path('correo/', CorreoView.as_view(), name='correo-list'),
    path('correo/<str:pk>', CorreoDetailView.as_view(), name='correo-detail'),

    path('telefono/', TelefonoView.as_view(), name='telefono-list'),
    path('telefono/<str:pk>', TelefonoDetalleView.as_view(), name='telefono-detail'),

    path('operador/', OperadorView.as_view(), name='operador-list'),

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
    path('provincia/<int:id_departamento>/', ProvinciaView.as_view(), name='provincia-list'),
    path('distrito/<int:id_provincia>/', DistritoView.as_view(), name='distrito-list'),
    path('tipo_via/', TipoViaView.as_view(), name='tipo-via-list'),
    path('tipo_zona/', TipoZonaView.as_view(), name='tipo-zona-list'),
    
    path('personaJuridica', PersonaJuridicaView.as_view(), name="perona-list"),
    path('personaJuridica/<str:pk>', PersnaJuridicaDetailView.as_view(), name="persona-detail"),

    path('personaNatural', PersonaNaturalView.as_view(), name="perona-list"),
    path('personaNatural/<str:pk>', PersonaNaturalDetailView.as_view(), name="persona-detail"),
    path('genero/', GeneroView.as_view(), name='genero-list')
]

