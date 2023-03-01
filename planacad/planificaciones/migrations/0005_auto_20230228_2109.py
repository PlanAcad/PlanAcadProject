# Generated by Django 2.2 on 2023-03-01 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0004_auto_20230227_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='indicadores_de_logro',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_clase',
            field=models.DateField(blank=True, default=datetime.date(2023, 2, 28), null=True),
        ),
    ]
