# Generated by Django 2.2 on 2021-09-02 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_carrera', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DatosDescriptivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('institucion', models.CharField(blank=True, max_length=50, null=True)),
                ('departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('area_bloque', models.CharField(blank=True, max_length=50, null=True)),
                ('porcentaje_horas_en_carrera', models.CharField(blank=True, max_length=50, null=True)),
                ('porcentaje_horas_en_area', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel', models.CharField(blank=True, max_length=50, null=True)),
                ('ciclo_lectivo', models.IntegerField(blank=True, null=True)),
                ('carga_horaria_total', models.FloatField(blank=True, max_length=50, null=True)),
                ('carga_horaria_semanal', models.FloatField(blank=True, max_length=50, null=True)),
                ('cursado', models.CharField(blank=True, choices=[('A', 'Anual'), ('1', '1er Cuatrimestre'), ('2', '2do Cuatrimestre')], default='A', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fundamentacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fundamentos', models.CharField(max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('situacion', models.CharField(max_length=50)),
                ('dedicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='asignatura',
            old_name='nombreMateria',
            new_name='nombre_materia',
        ),
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now=True, max_length=50)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Asignatura')),
                ('datos_descriptivos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.DatosDescriptivos')),
                ('fundamentacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Fundamentacion')),
            ],
        ),
        migrations.AddField(
            model_name='datosdescriptivos',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Asignatura'),
        ),
        migrations.AddField(
            model_name='datosdescriptivos',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Carrera'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Carrera'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ManyToManyField(to='planificaciones.Profesor'),
        ),
    ]