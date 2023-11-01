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
from django.urls import path
from login import views as login_views
from administracionProyecto import views as administracionProyecto_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.home, name='home'),
    path('signup/', login_views.signup, name='signup'),
    path('logout/', login_views.signout, name='logout'),
    path('signin/', login_views.signin, name='signin'),
    path('gestionar_proyecto/', administracionProyecto_views.gestionar, name='gestionar_proyecto'),
    path('gestionar_proyecto/crear_proyecto/', administracionProyecto_views.crearProyecto, name='crear_proyecto'),
    path('gestionar_proyecto/proyecto/<int:id>/', administracionProyecto_views.proyecto, name='proyecto'),
    path('gestionar_proyecto/editarProyecto/<int:id>/', administracionProyecto_views.editarProyecto, name='editarProyecto'),
    path('gestionar_proyecto/eliminarProyecto/<int:id>/', administracionProyecto_views.eliminarProyecto, name='eliminarProyecto'),
    path('gestionar_proyecto/proyecto/<int:id>/aprobarProyecto/', administracionProyecto_views.aprobarProyecto, name='aprobarProyecto'),
    path('listaTarea/', administracionProyecto_views.listaTarea, name='listaTarea'),
    path('listaTarea/crearTarea/', administracionProyecto_views.crearTarea, name='crearTarea'),
    path('listaTarea/editarTarea/<int:id>/', administracionProyecto_views.editarTarea, name='editarTarea'),
    path('listaTarea/eliminarTarea/<int:id>/', administracionProyecto_views.eliminarTarea, name='eliminarTarea'),
    path('listaRecurso/', administracionProyecto_views.listaRecurso, name = 'listaRecurso'),
    path('listaRecurso/agregarRecurso/', administracionProyecto_views.agregarRecurso, name = 'agregarRecurso'),
    path('listaRecurso/editarRecurso/<int:id>/', administracionProyecto_views.editarRecurso, name = 'editarRecurso'),
    path('listaRecurso/eliminarRecurso/<int:id>/', administracionProyecto_views.eliminarRecurso, name = 'eliminarRecurso'),
]
