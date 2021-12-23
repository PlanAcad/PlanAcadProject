# Generated by Django 2.2 on 2021-12-22 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0034_auto_20211221_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='fecha_clase',
            field=models.DateField(blank=True, default=datetime.date(2021, 12, 22), null=True),
        ),
        migrations.AlterField(
            model_name='clase',
            name='resultado_de_aprendizaje',
            field=models.ManyToManyField(blank=True, null=True, to='planificaciones.ResultadoDeAprendizaje'),
        ),
        migrations.AlterField(
            model_name='clase',
            name='unidad_tematica_o_tema',
            field=models.ManyToManyField(blank=True, null=True, to='planificaciones.Contenido'),
        ),
    ]