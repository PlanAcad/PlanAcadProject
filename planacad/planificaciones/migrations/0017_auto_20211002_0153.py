# Generated by Django 3.2.6 on 2021-10-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0016_auto_20210930_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='planificacion',
            name='numero_comisiones',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='numero_estudiantes_comision',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
