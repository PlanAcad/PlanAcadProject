# Generated by Django 2.2 on 2023-01-20 22:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0048_auto_20230114_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidad',
            name='planificacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Planificacion'),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='carrera', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_clase',
            field=models.DateField(blank=True, default=datetime.date(2023, 1, 20), null=True),
        ),
    ]