# Generated by Django 5.0 on 2024-10-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0003_persona_numero_visa1_persona_numero_visa2'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='ciudad_banco',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Ciudad Banco'),
        ),
        migrations.AddField(
            model_name='persona',
            name='codigo_corto_banco',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Códico corto del Banco'),
        ),
    ]
