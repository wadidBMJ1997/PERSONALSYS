# Generated by Django 5.0 on 2024-10-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0009_detalleproyecto_email_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='vessel_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre del Vhiculo'),
        ),
    ]
