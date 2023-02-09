# Generated by Django 3.2.6 on 2021-10-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0018_detalleprofesorcatedra_actividades'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialBibliografico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('titulo_libro', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=200)),
                ('año_publicacion', models.CharField(max_length=5)),
                ('nombre_capitulo', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('es_obligatorio', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='planificacion',
            name='material_bibliografico',
            field=models.ManyToManyField(to='planificaciones.MaterialBibliografico'),
        ),
    ]
