# Generated by Django 2.2 on 2021-09-22 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0011_auto_20210921_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCompetencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Competencia')),
            ],
        ),
    ]
