from django.urls import path
from . import views

urlpatterns = [
    path('gestionar_proyecto/', views.gestionar, name='gestionar_proyecto'),
    path('gestionar_proyecto/crear_proyecto/', views.crearProyecto, name='crear_proyecto'),
    path('gestionar_proyecto/proyecto/<int:id_proyecto>/', views.verProyecto, name='ver_proyecto'),
    path('gestionar_proyecto/editarProyecto/<int:id>/', views.editarProyecto, name = 'editarProyecto'),
    path('gestionar_proyecto/eliminarProyecto/<int:id>/', views.eliminarProyecto, name = 'eliminarProyecto'),
    path('gestionar_proyecto/proyecto/<int:id_proyecto>/aprobarProyecto/', views.aprobarProyecto, name = 'aprobarProyecto'),
]

