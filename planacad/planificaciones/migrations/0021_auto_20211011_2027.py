# Generated by Django 3.2.6 on 2021-10-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0020_alter_planificacion_material_bibliografico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialbibliografico',
            name='editor',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='materialbibliografico',
            name='nombre_capitulo',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='materialbibliografico',
            name='ubicacion',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
