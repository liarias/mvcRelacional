from .models import *
from rest_framework import serializers


class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = ( 'id', 'nombre','contrato')


class PersonaSerializer(serializers.ModelSerializer):
	servicios = ServicioSerializer(read_only=True, many=True)
	class Meta:
		model = Persona
		fields = ( 'id', 'nombre','servicios')
