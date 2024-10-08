# Generated by Django 5.0.7 on 2024-08-25 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0002_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraAlimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.IntegerField()),
                ('cantidad_producto', models.IntegerField()),
                ('total_peso', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_kilo', models.DecimalField(decimal_places=20, max_digits=30)),
            ],
            options={
                'verbose_name': 'Compra Alimento',
                'verbose_name_plural': 'Compras Alimentos',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=50)),
                ('abreviatura', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
            },
        ),
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('marca', models.CharField(max_length=200)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Person.estado')),
                ('id_unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AlimentoPro.unidadmedida')),
            ],
            options={
                'verbose_name': 'Alimento',
                'verbose_name_plural': 'Alimentos',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompAlimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('peso_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('costo_unidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('id_alimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AlimentoPro.alimentos')),
                ('id_comp_alim', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AlimentoPro.compraalimento')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Person.proveedor')),
            ],
            options={
                'verbose_name': 'Detalle de Compra de Alimento',
                'verbose_name_plural': 'Detalles de Compras de Alimentos',
            },
        ),
    ]
