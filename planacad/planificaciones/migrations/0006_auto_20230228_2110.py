# Generated by Django 2.2 on 2023-03-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0005_auto_20230228_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='tecnicas_de_evaluacion',
            field=models.CharField(max_length=3000),
        ),
    ]
