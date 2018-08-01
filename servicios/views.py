from django.shortcuts import render
from .models import *
#####
from rest_framework import viewsets
from servicios.serializers import PersonaSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = datosCsv.objects.all()
    queryset = queryset[:25] 
    serializer_class = PersonaSerializer


########
def serviciosListar(request):
	personas=Persona.objects.all()
	return render(request,'servicios/usuario.html',{'personas':personas})

def serviciosFiltro(request):
	datos=datosCsv.objects.all()
	datos = datos[:3000]
	return render(request,'servicios/servicios.html',{'datos':datos})
