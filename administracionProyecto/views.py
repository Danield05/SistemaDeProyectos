from django.shortcuts import render, redirect
from .forms import FormTarea , FormRecurso, ProyectoForm
from .models import Tarea, Recurso, Proyecto
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

def listaTarea(request):
    tarea = Tarea.objects.all()
    return render(request, 'listaTarea.html',{'tarea': tarea})

def crearTarea(request):
    if request.method == 'GET':
        usuario = User.objects.all()
        return render(request,'crearTarea.html', {
            'usuario': usuario,
            'form': FormTarea
        })
    else:
        form = FormTarea(request.POST)
        nuevaTarea = form.save(commit=False)
        nuevaTarea.usuario = User.objects.get(username=nuevaTarea.encargado)

        nuevaTarea.save()
        return redirect('listaTarea')

def editarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    usuario = User.objects.all()
    
    if request.method == 'POST':
        form = FormTarea(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect(reverse('listaTarea'))
    
    # Si la solicitud no es un POST o el formulario no es válido, renderiza la página de edición nuevamente
    return render(request, 'editarTarea.html', {
        'form': FormTarea(instance=tarea),
        'usuario': usuario
    })
    
def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()   
    return redirect(to='listaTarea') 

def listaRecurso(request):
    recurso = Recurso.objects.all()
    return render(request, 'listaRecurso.html', {'recurso': recurso})

def agregarRecurso(request):
    if request.method == 'GET':
        return render(request,'agregarRecurso.html', {
            'form': FormRecurso
        })
    else:
        form = FormRecurso(request.POST)
        nuevoRecurso = form.save(commit=False)
        nuevoRecurso.save()
        return redirect('listaRecurso')
    
def editarRecurso(request, id):
    recurso = Recurso.objects.get(id=id)
    if request.method == 'POST':
        form = FormRecurso(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect(reverse('listaRecurso'))
    return render(request, 'editarRecurso.html', {
        'form': FormRecurso(instance=recurso)
    }) 
    
def eliminarRecurso(request, id):
    recurso = Recurso.objects.get(id=id)
    recurso.delete()   
    return redirect(to='listaRecurso') 

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