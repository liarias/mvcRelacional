from .models import *
from rest_framework import serializers


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=False, allow_blank=True, max_length=100)
    servicio=serializers.CharField(required=False, allow_blank=True, max_length=100)
    ciudad=serializers.CharField(required=False, allow_blank=True, max_length=100)
    fecha=serializers.DateField()
    numero=serializers.IntegerField()

    class Meta:
        model = datosCsv
        fields = ('id', 'nombre', 'servicio','ciudad','fecha','numero')
