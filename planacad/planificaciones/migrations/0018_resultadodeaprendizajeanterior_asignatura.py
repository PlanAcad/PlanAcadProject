# Generated by Django 2.2 on 2021-10-12 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0017_resultadodeaprendizajeanterior'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadodeaprendizajeanterior',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Asignatura'),
        ),
    ]
