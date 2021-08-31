# Generated by Django 2.2 on 2021-08-27 19:36

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('planificaciones', '0010_auto_20210827_1018'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seccion1',
            new_name='DatosDescriptivos',
        ),
        migrations.RenameModel(
            old_name='Seccion3',
            new_name='Fundamentacion',
        ),
        migrations.RenameField(
            model_name='asignatura',
            old_name='nombreMateria',
            new_name='nombre_materia',
        ),
        migrations.RenameField(
            model_name='carrera',
            old_name='nombreCarrera',
            new_name='nombre_carrera',
        ),
        migrations.RenameField(
            model_name='datosdescriptivos',
            old_name='areaBloque',
            new_name='area_bloque',
        ),
        migrations.RenameField(
            model_name='datosdescriptivos',
            old_name='cargaHorariaSemanal',
            new_name='carga_horaria_semanal',
        ),
        migrations.RenameField(
            model_name='datosdescriptivos',
            old_name='cargaHorariaTotal',
            new_name='carga_horaria_total',
        ),
        migrations.RenameField(
            model_name='datosdescriptivos',
            old_name='cicloLectivo',
            new_name='ciclo_lectivo',
        ),
        migrations.RenameField(
            model_name='datosdescriptivos',
            old_name='porcentajeHorasenArea',
            new_name='porcentaje_horas_en_area',
        ),
        migrations.RenameField(
            model_name='datosdescriptivos',
            old_name='porcentajeHorasenCarrera',
            new_name='porcentaje_horas_en_carrera',
        ),
        migrations.RenameField(
            model_name='planificacion',
            old_name='seccion1',
            new_name='datos_descriptivos',
        ),
        migrations.RenameField(
            model_name='planificacion',
            old_name='fechaCreacion',
            new_name='fecha_creacion',
        ),
        migrations.RenameField(
            model_name='planificacion',
            old_name='seccion3',
            new_name='fundamentacion',
        ),
    ]
