# Generated by Django 2.2 on 2021-09-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0003_planificacion_eliminar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planificacion',
            name='eliminar',
        ),
        migrations.AddField(
            model_name='planificacion',
            name='eliminada',
            field=models.BooleanField(default=False),
        ),
    ]
