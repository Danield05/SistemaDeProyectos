from django.urls import path
from . import views

urlpatterns = [
    path('listaTarea/', views.listaTarea, name = 'listaTarea'),
    path('listaTarea/crearTarea/', views.crearTarea, name = 'crearTarea'),
]
