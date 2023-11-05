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
from django.shortcuts import redirect
from django.urls import path,include
from login import views as login_views
from administracionProyecto import views as administracionProyecto_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('login.urls')),
    path('gestionar_proyecto/', administracionProyecto_views.gestionar, name='gestionar_proyecto'),
    path('gestionar_proyecto/crear_proyecto/', administracionProyecto_views.crearProyecto, name='crear_proyecto'),
    path('gestionar_proyecto/proyecto/<int:id>/', administracionProyecto_views.proyecto, name='proyecto'),
    path('gestionar_proyecto/editarProyecto/<int:id>/', administracionProyecto_views.editarProyecto, name='editarProyecto'),
    path('gestionar_proyecto/eliminarProyecto/<int:id>/', administracionProyecto_views.eliminarProyecto, name='eliminarProyecto'),
    path('gestionar_proyecto/proyecto/<int:id>/aprobarProyecto/', administracionProyecto_views.aprobarProyecto, name='aprobarProyecto'),
    path('listaTarea/', administracionProyecto_views.listaTarea, name='listaTarea'),
    path('listaTarea/<int:id>/', administracionProyecto_views.listaTarea, name='listaTarea'),
    path('listaTarea/crearTarea/<int:id>/', administracionProyecto_views.crearTarea, name='crearTarea'),
    path('listaTarea/editarTarea/<int:id>/', administracionProyecto_views.editarTarea, name='editarTarea'),
    path('listaTarea/eliminarTarea/<int:id>/', administracionProyecto_views.eliminarTarea, name='eliminarTarea'),
    path('listaRecurso/', administracionProyecto_views.listaRecurso, name = 'listaRecurso'),
    path('listaRecurso/<int:id>/', administracionProyecto_views.listaRecurso, name = 'listaRecurso'),
    path('listaRecurso/agregarRecurso/<int:id>/', administracionProyecto_views.agregarRecurso, name = 'agregarRecurso'),
    path('listaRecurso/editarRecurso/<int:id>/', administracionProyecto_views.editarRecurso, name = 'editarRecurso'),
    path('listaRecurso/eliminarRecurso/<int:id>/', administracionProyecto_views.eliminarRecurso, name = 'eliminarRecurso'),
    path('listaReporte/', administracionProyecto_views.listaReporte, name = 'listaReporte'),
    path('listaReporte/<int:id>/', administracionProyecto_views.listaReporte, name = 'listaReporte'),
    path('listaReporte/editarReporte/<int:id>/', administracionProyecto_views.editarReporte, name = 'editarReporte'),
    path('listaReporte/eliminarReporte/<int:id>/', administracionProyecto_views.eliminarReporte, name = 'eliminarReporte'),
    path('listaReporte/crearReporte/<int:id>/', administracionProyecto_views.crearReporte, name = 'crearReporte'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
