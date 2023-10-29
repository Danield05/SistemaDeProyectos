from django.urls import path
from . import views

urlpatterns = [
    path('gestionar_proyecto/', views.gestionar, name='gestionar_proyecto'),
    path('gestionar_proyecto/crear_proyecto/', views.crearProyecto, name='crear_proyecto'),
]

