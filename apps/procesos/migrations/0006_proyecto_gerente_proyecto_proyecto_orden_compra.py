# Generated by Django 5.0 on 2024-09-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0005_alter_proyecto_observaciones_proyecto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='gerente_proyecto',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Gerente Proyecto'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='orden_compra',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Orden Compra'),
        ),
    ]