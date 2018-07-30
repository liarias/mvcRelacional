from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.serviciosListar,name='usuarios'),
    path(r'servicios/',views.serviciosFiltro,name='servicios')
]
