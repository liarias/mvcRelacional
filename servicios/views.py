from django.shortcuts import render
from .models import *
#####
from servicios.serializers import *

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics


class ServicioViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer




########
def personaListar(request):
	personas=Persona.objects.all()
	return render(request,'servicios/usuario.html',{'personas':personas})
def servicioListar(request):
    personas=Persona.objects.all()
    return render(request,'servicios/servicios.html',{'personas':personas})
def contratosListar(request):
    contratos=Contrato.objects.all()
    return render(request,'servicios/servicios.html',{'contratos':contratos})

def personaDetalle(request,pk):
    persona=Persona.objects.get(pk=pk)
    return render(request,'servicios/personaDetalle.html',{'persona':persona})
def servicioCrear(request,pk):
    servicio=Persona.objects.get(pk=pk)
    return render(request,'servicios/servicioCrear.html',{'servicio':servicio})
def servicioModificar(request,pk):
    servicio=Persona.objects.get(pk=pk)
    return render(request,'servicios/servicioModificar.html',{'servicio':servicio})



class PersonaListar(APIView):
    
    def get(self, request, format=None):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicioListar(APIView):
    
    def get(self, request, format=None):
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@permission_classes((permissions.AllowAny,))
class DetalleServicio(APIView):
    def get_object(self, pk):
        try:
            return Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):

        servicio = self.get_object(pk)
        serializer = ServicioSerializer(servicio)
        print("AHHHHHHHHHHHHHHHHHHHH")
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        servicio = self.get_object(pk)
        serializer = ServicioSerializer(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        servicio = self.get_object(pk)
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((permissions.AllowAny,))
class DetallePersona(APIView):
    def get_object(self, pk):
        try:

            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona)

        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)