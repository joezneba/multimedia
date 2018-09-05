from django.urls import path
from apps.video import views

urlpatterns = [
    path('rep/<int:id_video>', views.reproductor, name='reproductor'),
    path('categoria/<int:id_categoria>', views.filtroCategorias, name='filtroCategorias'),
    path('busqueda_video', views.buscarVideo, name='busquedaVideo'),
]