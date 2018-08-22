from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url, include

from servicios.views import *

from servicios import views


urlpatterns = [
    path(r'', views.PersonaListar.as_view(),name='usuarios'),
    path(r'servicios/',views.ServicioListar.as_view(),name='servicios'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.personaDetalle, name="personaDetalle"),
    url(r'^servicio/crear/(?P<pk>[0-9]+)/$', views.DetalleServicio.as_view(), name="servicioCrear"),
    url(r'^servicio/modificar/(?P<pk>[0-9]+)/$', views.DetalleServicio.as_view(), name="servicioModificar"),
    url(r'^servicio/crear/(?P<pk>[0-9]+)/$', views.ServicioListar.as_view(), name="crearServicio"),
    path(r'servicio/modificado/', views.modificado, name="modificado"),
    path(r'iniciarSesion/',views.iniciarSesion,name='iniciarSesion'),
	path(r'SalirSesion/',views.salirSesion,name='salirSesion'),


]

urlpatterns = format_suffix_patterns(urlpatterns)