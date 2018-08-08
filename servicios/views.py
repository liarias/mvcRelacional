from django.shortcuts import render
from .models import *
#####
from rest_framework import viewsets
from servicios.serializers import PersonaSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def tablaDeUsuarios(request):
    if request.method == 'GET':
        personas = Persona.objects.all()
        eturn render(request,'servicios/usuario.html',{'personas':personas})


@api_view(['GET','PUT'])
@permission_classes((permissions.AllowAny,))
def serviciosUsuario(request,pk):
    try:
        user = Usuario.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serviciosDeUsuario = Usuario_Servicio.objects.filter(usuario=pk)
        return render(request,'aplicacion/tabla.html',{'user':user,'datos':serviciosDeUsuario})

class PersonaViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    personas = Persona.objects.all()
    personas = personas[:25] 
    serializer_class = PersonaSerializer


########
def serviciosListar(request):
	personas=Persona.objects.all()
	return render(request,'servicios/usuario.html',{'personas':personas})

def serviciosFiltro(request):
	datos=datosCsv.objects.all()
	datos = datos[:3000]
	return render(request,'servicios/servicios.html',{'datos':datos})
