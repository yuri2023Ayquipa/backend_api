from django.db import models



# Create your models here.
class CompraAlimento(models.Model):
    class Meta:
        verbose_name = 'Compra Alimento'
        verbose_name_plural = 'Compras Alimentos'

    lote = models.IntegerField(null=False)
    cantidad_producto = models.IntegerField(null=False)
    total_peso = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    costo_total = models.DecimalField(max_digits=10,decimal_places=2)
    precio_kilo = models.DecimalField(max_digits=30, decimal_places=20)

    