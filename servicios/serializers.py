from .models import *
from rest_framework import serializers

class ContratoSerializer(object):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField(allow_blank=False,max_length=200)
    fecha = serializers.DateTimeField()
    def create(self, validated_data):
        """
        Create and return a new `Servicio` instance, given the validated data.
        """
        return Contrato.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Servicio` instance, given the validated data.
        """
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.fecha= validated_data.get('fecha', instance.fecha)
        instance.save()
        return instance

class ServicioSerializer(object):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(allow_blank=False,max_length=200)
    contrato = ContratoSerializer(many=True)
    def create(self, validated_data):
        """
        Create and return a new `Servicio` instance, given the validated data.
        """
        return Servicio.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Servicio` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.contrato = validated_data.get('nombre', instance.contrato)
        instance.save()
        return instance

class PersonaSerializer(object):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(allow_blank=False,max_length=200)
    apellido = serializers.CharField(allow_blank=False,max_length=200)
    servicios = ServicioSerializer(many=True)
    def create(self, validated_data):
        """
        Create and return a new `Usuario` instance, given the validated data.
        """
        return Persona.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Usuario` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.servicios = validated_data.get('servicios', instance.servicios)

        instance.save()
        return instance

