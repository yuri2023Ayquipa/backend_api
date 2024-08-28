from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

from apps.User.login import Login, Logout

schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion de API",
        default_version='v1',
        description="Note API built by CodevoWeb",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ayquipa26-04@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )
from apps.menu.views import MenuViews, MenuDetail_views

from apps.Person.views.views_estado import EstadoView
from apps.Person.views.views_person import PersonaView, PersonaDetailView
from apps.Person.views.views_proveedor import ProveedorView, ProveedorDetailView
from apps.Person.views.views_tipo_contribuyente import TipoContribuyenteView 
from apps.Person.views.views_tipo_documento import TipoDocumentoView
from apps.Person.views.views_origen_entidad import OrigenEntidadView
from apps.Person.views.views_nacionalidad import NacionalidadView
from apps.Person.views.views_cond_domiciliaria import CondicionDomiciliadoView
from apps.Person.views.views_correo import CorreoView, CorreoDetailView
from apps.Person.views.views_operador import OperadorView
from apps.Person.views.views_telefono import TelefonoView, TelefonoDetalleView
from apps.Person.views.views_direccion import DireccionView, DireccionDetalleView
from apps.Person.views.views_departamento import DepartamentoView
from apps.Person.views.views_provincia import ProvinciaView
from apps.Person.views.views_distrito import DistritoView
from apps.Person.views.views_tipo_via import TipoViaView
from apps.Person.views.views_tipo_zona import TipoZonaView
from apps.Person.views.views_person_juridica import PersonaJuridicaView, PersnaJuridicaDetailView
from apps.Person.views.views_person_natural import PersonaNaturalView, PersonaNaturalDetailView
from apps.Person.views.views_genero import GeneroView

from apps.User.views import UserView, UserDetailView

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('admin/', admin.site.urls),
    path('api/menu/', MenuViews.as_view()),
    path('api/menu/<str:pk>', MenuDetail_views.as_view()),
    # end Person
    path('api/estado/', EstadoView.as_view(), name='estado-list'),
    path('api/correo/', CorreoView.as_view(), name='correo-list'),
    path('api/correo/<str:pk>', CorreoDetailView.as_view(), name='correo-detail'),
    path('api/telefono/', TelefonoView.as_view(), name='telefono-list'),
    path('api/telefono/<str:pk>', TelefonoDetalleView.as_view(), name='telefono-detail'),
    path('api/operador/', OperadorView.as_view(), name='operador-list'),
    path('api/direccion/', DireccionView.as_view(), name='direccion-list'),
    path('api/direccion/<str:pk>', DireccionDetalleView.as_view(), name='direccion-detail'),
    path('api/persona/', PersonaView.as_view(), name='persona-list'),
    path('api/persona/<str:pk>', PersonaDetailView.as_view(), name='persona-detail'),
    path('api/proveedor/', ProveedorView.as_view(), name='proveedor-list'),
    path('api/proveedor/<str:pk>',ProveedorDetailView.as_view(), name='proveedor'),
    path('api/tipo_documento/', TipoDocumentoView.as_view(), name='documento-list'),
    path('api/tipo_contribuyente/', TipoContribuyenteView.as_view(), name='contribuyente-list'),
    path('api/origen_entidad/', OrigenEntidadView.as_view(), name='origen-list'),
    path('api/nacionalidad/', NacionalidadView.as_view(), name='nacionalidad-list'),
    path('api/condicion_domiciliado/', CondicionDomiciliadoView.as_view(), name='condicion-list'),
    path('api/departamento/', DepartamentoView.as_view(), name='departamento-list'),
    path('api/provincia/<int:id_departamento>/', ProvinciaView.as_view(), name='provincia-list'),
    path('api/distrito/<int:id_provincia>/', DistritoView.as_view(), name='distrito-list'),
    path('api/tipo_via/', TipoViaView.as_view(), name='tipo-via-list'),
    path('api/tipo_zona/', TipoZonaView.as_view(), name='tipo-zona-list'),
    path('api/personaJuridica/', PersonaJuridicaView.as_view(), name="perona-list"),
    path('api/personaJuridica/<str:pk>', PersnaJuridicaDetailView.as_view(), name="persona-detail"),
    path('api/personaNatural/', PersonaNaturalView.as_view(), name="perona-list"),
    path('api/personaNatural/<str:pk>', PersonaNaturalDetailView.as_view(), name="persona-detail"),
    path('api/genero/', GeneroView.as_view(), name='genero-list'),
    #fin Person
    path('api/user/', UserView.as_view()),
    path('api/user/<str:pk>', UserDetailView.as_view()),
    path('api/login',Login.as_view(), name= 'login'),
    path('api/logout',Logout.as_view(), name= 'logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

