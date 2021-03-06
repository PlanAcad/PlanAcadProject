# Generated by Django 2.2 on 2021-09-17 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0002_remove_profesor_situacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dedicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dedicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Situacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('situacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TareasFunciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tarea_funcion', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoDeAprendizajes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resultado', models.CharField(max_length=50)),
                ('asignatura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Asignatura')),
                ('planificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Planificacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProfesorCatedra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Categoria')),
                ('dedicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Dedicacion')),
                ('planificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Planificacion')),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Profesor')),
                ('situacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Situacion')),
                ('tareas', models.ManyToManyField(blank=True, to='planificaciones.TareasFunciones')),
            ],
        ),
    ]
