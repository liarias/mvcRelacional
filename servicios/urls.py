from django.urls import path
from . import views

from django.conf.urls import url, include

from servicios.views import *
from rest_framework import renderers

from rest_framework.routers import DefaultRouter
from servicios import views


urlpatterns = [
    path(r'', views.personaListar,name='usuarios'),
    path(r'servicios/',views.servicioListar,name='servicios'),
    path(r'contratos/',views.contratosListar,name='contrato'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.personaDetalle, name="detallePersona"),
    url(r'^servicio/crear/(?P<pk>[0-9]+)/$', views.servicioCrear, name="servicioCrear"),
    url(r'^servicio/modificar/(?P<pk>[0-9]+)/$', views.servicioModificar, name="servicioModificar"),

]
