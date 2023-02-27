# Generated by Django 2.2 on 2023-02-27 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0003_auto_20230225_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='fecha_clase',
            field=models.DateField(blank=True, default=datetime.date(2023, 2, 27), null=True),
        ),
        migrations.AlterField(
            model_name='tareasfunciones',
            name='tarea_funcion',
            field=models.CharField(max_length=3000),
        ),
    ]