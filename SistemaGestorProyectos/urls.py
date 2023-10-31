"""
URL configuration for SistemaGestorProyectos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login import views as login_views
from gestionarProyecto import views as gestionarProyecto_views
from administrarProyecto import views as administrarProyecto_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('login.urls')),
    path('gestionar_proyecto/', gestionarProyecto_views.gestionar, name='gestionar_proyecto'),
    path('gestionar_proyecto/crear_proyecto/', gestionarProyecto_views.crearProyecto, name='crear_proyecto'),
    path('listaTarea/', administrarProyecto_views.listaTarea, name='listaTarea'),
    path('listaTarea/crearTarea/', administrarProyecto_views.crearTarea, name='crearTarea'),
    path('listaTarea/editarTarea/<int:id>/', administrarProyecto_views.editarTarea, name='editarTarea'),
    path('listaTarea/eliminarTarea/<int:id>/', administrarProyecto_views.eliminarTarea, name='eliminarTarea'),
]
