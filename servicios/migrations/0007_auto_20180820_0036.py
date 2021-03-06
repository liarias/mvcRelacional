# Generated by Django 2.0.7 on 2018-08-20 05:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_auto_20180812_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='contrato',
        ),
        migrations.AddField(
            model_name='servicio',
            name='ciudad',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='servicio',
            name='direccion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='servicio',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='pago',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Contrato',
        ),
    ]
