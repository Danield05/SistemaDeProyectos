from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProyectoForm
from .models import Proyecto
from django.contrib.auth.models import User
from django.urls import reverse

def gestionar(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestionarProyecto.html', {'proyectos': proyectos})


def crearProyecto(request):
    if request.method == 'GET':
        usuario = User.objects.all()
        proyecto = Proyecto.objects.all()
        return render(request,'crearProyecto.html', {
            'usuario': usuario,
            'proyecto': proyecto,
            'form': ProyectoForm
        })
    else:
        form = ProyectoForm(request.POST)
        if form.is_valid():
            nuevoProyecto = form.save(commit=False)
            nuevoProyecto.save()
        return redirect('gestionar_proyecto') 
  
def editarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect(reverse('gestionar_proyecto'))
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'editarProyecto.html', {'form': form})
    
def proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    return render(request, 'proyecto.html', {'proyecto': proyecto})

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect(to='gestionar_proyecto')

def aprobarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        proyecto.aprobado = True
        proyecto.save()
        return redirect(reverse('proyecto', args=[proyecto.id]))
    return render(request, 'proyecto.html', {'proyecto': proyecto})
