from django.urls import path
from apps.usuario import views

urlpatterns = [
    path('registro', views.registro, name='registro'),
    path('comprobarPerfil', views.comprobarPerfil, name='comprobarPerfil'),
    path('crearPerfil', views.crearPerfil, name='crearPerfil')
]