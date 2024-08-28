from django.contrib import admin

from .models.models_detalle_comp_gand import DetalleCompraGanado
from .models.models_ganado import Ganado
from .models.models_ganado_comp import GanadoCompra
from .models.models_sexo_ganado import SexoGanado
# Register your models here.
admin.site.register(DetalleCompraGanado)
admin.site.register(Ganado)
admin.site.register(GanadoCompra)
admin.site.register(SexoGanado)