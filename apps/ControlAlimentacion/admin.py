from django.contrib import admin

from .models.models_alimentacion_diaria import Alimentacion
from .models.models_detalle_alimentacion import DetalleAlimentacion
from .models.models_corral import Corral
from .models.models_detalle_corral import DetalleGanadoCorral
# Register your models here.
admin.site.register(Alimentacion)
admin.site.register(DetalleAlimentacion)
admin.site.register(Corral)
admin.site.register(DetalleGanadoCorral)