from django.shortcuts import render
from .models import *

def serviciosListar(request):
	personas=Persona.objects.all()
	return render(request,'servicios/usuario.html',{'personas':personas})

def serviciosFiltro(request):
	datos=datosCsv.objects.all()
	datos = datos[:3000]
	return render(request,'servicios/servicios.html',{'datos':datos})
