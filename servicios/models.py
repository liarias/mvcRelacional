from django.db import models

class Servicio(models.Model):
	nombre = models.CharField(max_length=100)

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	servicios = models.ManyToManyField(Servicio)

class datosCsv(models.Model):
	nombre=models.CharField(max_length=200)
	servicio=models.CharField(max_length=100)
	ciudad=models.CharField(max_length=100)
	fecha=models.DateField()
	numero=models.IntegerField()
