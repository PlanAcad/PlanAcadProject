# Generated by Django 2.2 on 2021-08-26 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0014_detalleprofesorcatedra_planificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareasfunciones',
            old_name='detalleprofesorcatedra',
            new_name='detalle_profesor_catedra',
        ),
        migrations.RenameField(
            model_name='tareasfunciones',
            old_name='tareaFunciones',
            new_name='tarea_funcion',
        ),
    ]
