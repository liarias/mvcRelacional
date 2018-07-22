from django.db import models

class Servicio(models.Model):
	nombre = models.CharField(max_length=100)

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	servicios = models.ManyToManyField(Servicio)

