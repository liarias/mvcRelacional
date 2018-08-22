from django.db import models

class Servicio(models.Model):
	owner = models.ForeignKey('Persona', related_name='persona', on_delete=models.CASCADE, default='')
	nombre = models.CharField(max_length=100)
	ciudad=models.CharField(max_length=500, default='')
	direccion=models.CharField(max_length=500, default='')
	fecha=models.DateField()
	pago=models.IntegerField(default=0)
	def save(self, *args, **kwargs):
		if not self.id:
		    super(Servicio, self).save(*args, **kwargs)
		# process self.parent_subject (should be called ...subjects, semantically)
		super(Servicio, self).save(*args, **kwargs)
	
	def personas(self):
   		return self.persona_set.filter(servicio = self.pk)
   		
class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	servicios = models.ManyToManyField(Servicio)
	def get_servicios(self):
   		return self.servicio_set.all()
	