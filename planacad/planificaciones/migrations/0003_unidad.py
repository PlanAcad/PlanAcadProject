# Generated by Django 2.2 on 2021-09-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0002_remove_profesor_situacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_unidad', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=600)),
            ],
        ),
    ]
