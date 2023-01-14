# Generated by Django 2.2 on 2023-01-14 14:32

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planificaciones', '0047_auto_20230112_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_clase',
            field=models.DateField(blank=True, default=datetime.date(2023, 1, 14), null=True),
        ),
        migrations.DeleteModel(
            name='CarreraUsuario',
        ),
    ]
