# Generated by Django 3.2.6 on 2021-09-18 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0004_merge_20210918_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='CondicionAprobacionCursada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='CondicionAprobacionDirecta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=6000)),
            ],
        ),
        migrations.AddField(
            model_name='planificacion',
            name='condicion_aprobacion_cursada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.condicionaprobacioncursada'),
        ),
        migrations.AddField(
            model_name='planificacion',
            name='condicion_aprobacion_directa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.condicionaprobaciondirecta'),
        ),
    ]
