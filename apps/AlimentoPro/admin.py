from django.contrib import admin

from .models.models_alimento import Alimentos
from .models.models_unidad_medida import UnidadMedida
from .models.models_compra_alim import CompraAlimento
from .models.models_detalle_comp_alim import DetalleCompAlimento

# Register your models here.
admin.site.register(Alimentos)
admin.site.register(UnidadMedida)
admin.site.register(CompraAlimento)
admin.site.register(DetalleCompAlimento)