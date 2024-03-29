# Generated by Django 2.2 on 2023-01-05 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0041_auto_20230105_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correccion', models.CharField(max_length=500)),
                ('seccion', models.IntegerField(blank=True, default=1, null=True)),
                ('estado', models.CharField(blank=True, choices=[('G', 'Generado'), ('R', 'Resuelto')], max_length=15, null=True)),
                ('planificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Planificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=500)),
                ('correccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correcciones', to='planificaciones.Correccion')),
            ],
        ),
    ]
