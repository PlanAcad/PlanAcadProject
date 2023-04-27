# Generated by Django 2.2 on 2023-04-18 00:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planificaciones', '0008_auto_20230311_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='fechaDeCreacion',
            field=models.DateField(blank=True, default=datetime.date(2023, 4, 17), null=True),
        ),
        migrations.AddField(
            model_name='correccion',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creador_correccion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='correccion',
            name='fechaDeCreacion',
            field=models.DateField(blank=True, default=datetime.date(2023, 4, 17), null=True),
        ),
        migrations.AddField(
            model_name='correccion',
            name='usuarioQueResolvio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resolvio_correccion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_clase',
            field=models.DateField(blank=True, default=datetime.date(2023, 4, 17), null=True),
        ),
        migrations.AlterField(
            model_name='correccion',
            name='estado',
            field=models.CharField(blank=True, choices=[('G', 'Generado'), ('R', 'Resuelto'), ('C', 'Cerrado')], max_length=15, null=True),
        ),
    ]
