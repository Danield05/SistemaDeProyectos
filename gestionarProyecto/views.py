from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProyectoForm
from .models import Proyecto
from django.contrib.auth.models import User

def gestionar(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestionarProyecto.html', {'proyectos': proyectos})


def crearProyecto(request):
    if request.method == 'POST':
        form=ProyectoForm(request.POST)
        if form.is_valid():
            nuevoProyecto = form.save(commit=False)
            nuevoProyecto.nombre = form.cleaned_data['nombre']
            nuevoProyecto.objetivo = form.cleaned_data['objetivo']
            nuevoProyecto.prioridad = form.cleaned_data['prioridad']
            nuevoProyecto.fecha_inicio = form.cleaned_data['fecha_inicio']
            nuevoProyecto.fecha_fin = form.cleaned_data['fecha_fin']
            nuevoProyecto.presupuesto = form.cleaned_data['presupuesto']
            nuevoProyecto.encargadoProyecto = form.cleaned_data['encargadoProyecto']
            nuevoProyecto.save()
            nuevoProyecto.encargado = User.objects.get(username=nuevoProyecto.encargadoProyecto)
            nuevoProyecto.save()
        return redirect('gestionar_proyecto')
    else:
        form=ProyectoForm()
    proyecto = Proyecto.objects.all()
    usuario = User.objects.all()
    return render(request, 'crearProyecto.html',{
        'proyecto': proyecto,
        'usuario': usuario,
        'form': form
    })

def editarProyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.nombre = form.cleaned_data['nombre']
            proyecto.objetivo = form.cleaned_data['objetivo']
            proyecto.prioridad = form.cleaned_data['prioridad']
            proyecto.fecha_inicio = form.cleaned_data['fecha_inicio']
            proyecto.fecha_fin = form.cleaned_data['fecha_fin']
            proyecto.presupuesto = form.cleaned_data['presupuesto']
            proyecto.encargadoProyecto = form.cleaned_data['encargadoProyecto']
            proyecto.save()
            proyecto.encargado = User.objects.get(username=proyecto.encargadoProyecto)
            proyecto.save()
            return redirect('gestionar_proyecto')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'editarProyecto.html', {'form': form})
    
