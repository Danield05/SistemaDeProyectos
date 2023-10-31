from django.urls import path
from . import views

urlpatterns = [
    path('listaTarea/', views.listaTarea, name = 'listaTarea'),
    path('listaTarea/crearTarea/', views.crearTarea, name = 'crearTarea'),
    path('listaTarea/editarTarea/<int:id>/', views.editarTarea, name = 'editarTarea'),
    path('listaTarea/eliminarTarea/<int:id>/', views.eliminarTarea, name = 'eliminarTarea'),
]
