# Generated by Django 2.2 on 2023-02-25 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0002_auto_20230225_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosdescriptivos',
            name='dias',
            field=models.ManyToManyField(blank=True, to='planificaciones.DiasCursado'),
        ),
    ]