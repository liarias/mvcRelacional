import csv
import os
from servicios.models import datosCsv
with open('todosmisservicios.csv',newline='') as csvfile:
 spamreader = csv.reader(csvfile)
 for row in spamreader:
  lista = row[0].split(';')
  p = datosCsv()
  p.nombre = lista[0]
  p.servicio = lista[1]
  p.ciudad = lista[2]
  p.fecha = lista[3]
  p.numero = lista[4]
  p.save()