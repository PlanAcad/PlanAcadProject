# Generated by Django 2.2 on 2023-01-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0051_auto_20230121_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='unidad_tematica',
        ),
        migrations.AddField(
            model_name='actividad',
            name='unidad_tematica',
            field=models.ManyToManyField(to='planificaciones.Unidad'),
        ),
    ]
