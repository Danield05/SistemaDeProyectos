from django.urls import path
from . import views

urlpatterns = [
    path('listaTarea/', views.listaTarea, name = 'listaTarea'),
    path('listaTarea/<int:id>/', views.listaTarea, name = 'listaTarea'),
    path('listaTarea/crearTarea/<int:id>/', views.crearTarea, name = 'crearTarea'),
    path('listaTarea/editarTarea/<int:id>/', views.editarTarea, name = 'editarTarea'),
    path('listaTarea/eliminarTarea/<int:id>/', views.eliminarTarea, name = 'eliminarTarea'),
    path('listaRecurso/', views.listaRecurso, name = 'listaRecurso'),
    path('listaRecurso/<int:id>/', views.listaRecurso, name = 'listaRecurso'),
    path('listaRecurso/agregarRecurso/<int:id>/', views.agregarRecurso, name = 'agregarRecurso'),
    path('listaRecurso/editarRecurso/<int:id>/', views.editarRecurso, name = 'editarRecurso'),
    path('listaRecurso/eliminarRecurso/<int:id>/', views.eliminarRecurso, name = 'eliminarRecurso'),
    path('listaReporte/', views.listaReporte, name = 'listaReporte'),
    path('listaReporte/<int:id>/', views.listaReporte, name = 'listaReporte'),
    path('listaReporte/crearReporte/<int:id>/', views.crearReporte, name = 'crearReporte'),
    path('listaReporte/editarReporte/<int:id>/', views.editarReporte, name = 'editarReporte'),
    path('listaReporte/eliminarReporte/<int:id>/', views.eliminarReporte, name = 'eliminarReporte'),
    path('gestionar_proyecto/', views.gestionar, name='gestionar_proyecto'),
    path('gestionar_proyecto/crear_proyecto/', views.crearProyecto, name='crear_proyecto'),
    path('gestionar_proyecto/proyecto/<int:id_proyecto>/', views.proyecto, name='ver_proyecto'), #aqui tenia views.verProyecto
    path('gestionar_proyecto/editarProyecto/<int:id>/', views.editarProyecto, name = 'editarProyecto'),
    path('gestionar_proyecto/eliminarProyecto/<int:id>/', views.eliminarProyecto, name = 'eliminarProyecto'),
    path('gestionar_proyecto/proyecto/<int:id_proyecto>/aprobarProyecto/', views.aprobarProyecto, name = 'aprobarProyecto'),
]
