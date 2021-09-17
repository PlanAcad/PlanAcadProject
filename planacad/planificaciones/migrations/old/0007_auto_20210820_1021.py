# Generated by Django 2.2 on 2021-08-20 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificaciones', '0006_auto_20210818_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fundamentos', models.CharField(max_length=6000)),
            ],
        ),
        migrations.AddField(
            model_name='planificacion',
            name='Seccion3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planificaciones.Seccion3'),
        ),
    ]
