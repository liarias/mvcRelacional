from django.shortcuts import render, get_object_or_404,redirect,render_to_response
from .models import *
from servicios.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers,viewsets,generics,permissions,status
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout

def personaListar(request):
	personas=Persona.objects.all()
	return render(request,'servicios/usuario.html',{'personas':personas})
def servicioListar(request):
    personas=Persona.objects.all()
    return render(request,'servicios/servicios.html',{'personas':personas})
def contratosListar(request):
    contratos=Contrato.objectss.all()
    return render(request,'servicios/servicios.html',{'contratos':contratos})

def personaDetalle(request,pk):
    persona=Persona.objects.get(pk=pk)
    serializer=PersonaSerializer(persona)
    print(serializer.data)        
    return render(request,'servicios/personaDetalle.html',{'persona':persona})
def servicioCrear(request,pk):
    servicio=Persona.objects.get(pk=pk)
    return render(request,'servicios/servicioCrear.html',{'servicio':servicio})
def servicioModificar(request,pk):
    servicio=Persona.objects.get(pk=pk)
    return render(request,'servicios/servicioModificar.html',{'servicio':servicio})
def modificado(request):
    return render(request,'servicios/modificado.html',{})
def iniciarSesion(request):
    if request.method == 'POST':
        usuario = authenticate(request,username=request.POST.get('nombreUsuario'),password=request.POST.get('password'))
        if usuario is not None:
            login(request,usuario)
            return redirect("/")
        else:
            return render(request, 'servicios/iniciarSesion.html', {"mensaje":"Tu usuario y contraseña no coinciden. Intenta de nuevo."})
    return render(request, 'servicios/iniciarSesion.html',{"mensaje":""})

def salirSesion(request):
    logout(request)
    return redirect("/")

@permission_classes((permissions.AllowAny,))
class PersonaListar(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'servicios/usuario.html'
    def get(self, request, format=None):
                    
        personas = Persona.objects.all()
        return Response({"personas":personas})

    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class ServicioListar(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'servicios/servicios.html'
    
    def get(self, request, format=None):
        servicios = Servicio.objects.all()
        print(servicios)
        return Response({"servicios":servicios})

    def post(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class DetalleServicio(APIView):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'servicios/servicioModificar.html'
    def get(self, request, pk, format=None):
        servicio= Servicio.objects.get(pk=pk)
        print(request)
        serializer = ServicioSerializer(servicio)
        return Response({'serializer':serializer,'servicio': servicio})

    def post(self, request, pk, format=None):
        print("entra")
        servicio= Servicio.objects.get(pk=pk)
        serializer = ServicioSerializer(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'servicios/servicioModificar.html'
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