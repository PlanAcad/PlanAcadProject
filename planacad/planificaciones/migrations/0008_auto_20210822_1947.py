# Generated by Django 2.2 on 2021-08-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0007_remove_profesor_dedicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion1',
            name='cicloLectivo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]