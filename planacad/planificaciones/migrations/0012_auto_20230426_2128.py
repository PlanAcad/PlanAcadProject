# Generated by Django 2.2 on 2023-04-27 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0011_auto_20230426_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcompetencia',
            name='descripcion',
            field=models.CharField(default='test', max_length=300),
        ),
    ]