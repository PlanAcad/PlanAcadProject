# Generated by Django 2.2 on 2021-10-11 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0016_auto_20210930_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoDeAprendizajeAnterior',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('planificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Planificacion')),
                ('resultado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.ResultadoDeAprendizaje')),
            ],
        ),
    ]