# Generated by Django 2.2 on 2021-12-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0032_auto_20211220_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='fechacalendarioacademico',
            name='ciclo_lectivo',
            field=models.IntegerField(null=True),
        ),
    ]
