#from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static
from apps.User.login import Login, Logout
from rest_framework.authentication import TokenAuthentication 



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
    #authentication_classes=[TokenAuthentication],
    
    )

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),

    #path('admin/', admin.site.urls),
    path('api/menu/', include('apps.menu.urls')),
    path('api/', include('apps.Person.urls')),
    path('api/user/', include('apps.User.urls')),
    #path('api/api-token-auth/', views.obtain_auth_token),
    path('api/login',Login.as_view(), name= 'login'),
    path('api/logout',Logout.as_view(), name= 'logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

