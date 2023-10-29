from django.shortcuts import render, redirect
from .forms import ProyectoForm
from .models import Proyecto
# Create your views here.

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
            nuevoProyecto.save()
        return redirect('gestionar_proyecto')
    else:
        form=ProyectoForm()
    proyecto = Proyecto.objects.all()
    return render(request, 'crearProyecto.html',{
        'proyecto': proyecto,
        'form': form
    })