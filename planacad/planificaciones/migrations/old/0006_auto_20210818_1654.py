# Generated by Django 2.2 on 2021-08-18 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0005_auto_20210818_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion1',
            name='areaBloque',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Asignatura'),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='cargaHorariaSemanal',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='cargaHorariaTotal',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Carrera'),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='cicloLectivo',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='cursado',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='departamento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='institucion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='nivel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='porcentajeHorasenArea',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='seccion1',
            name='porcentajeHorasenCarrera',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
