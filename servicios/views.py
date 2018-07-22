from django.shortcuts import render
from .models import *

def serviciosListar(request):
	personas=Persona.objects.all()
	return render(request,'servicios/index.html',{'personas':personas})
