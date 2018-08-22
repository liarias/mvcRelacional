import csv
import os
from servicios.models import *
with open('todosmisservicios.csv',newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		lista = row[0].split(';')
		s = Servicio()
		p = Persona()
		p.nombre = lista[0]
		p.save()
		s.owner=p
		s.nombre = lista[1]
		s.ciudad = lista[2]
		s.direccion = ''
		s.fecha = lista[3]
		s.pago = lista[4]
		s.save()		
		p.servicios.add(s)
			