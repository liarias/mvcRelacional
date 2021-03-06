# Generated by Django 2.0.7 on 2018-08-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_auto_20180730_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='servicio',
            name='contrato',
            field=models.ManyToManyField(to='servicios.Contrato'),
        ),
    ]
