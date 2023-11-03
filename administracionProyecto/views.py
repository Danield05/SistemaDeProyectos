from django.shortcuts import render, redirect
from .forms import FormTarea , FormRecurso, ProyectoForm, FormReporte
from .models import Tarea, Recurso, Proyecto, Reporte
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def listaTarea(request, id):
    proyecto = Proyecto.objects.get(id=id)
    tarea = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'listaTarea.html',{'id':id,'tarea': tarea})

def crearTarea(request, id):
    if request.method == 'GET':
        usuario = User.objects.all()
        return render(request,'crearTarea.html', {
            'usuario': usuario,
            'id': id, #agregue esto para que se pueda redireccionar a la lista de tareas del proyecto
            'form': FormTarea
        })
    else:
        form = FormTarea(request.POST)
        if form.is_valid():
            nuevaTarea = form.save(commit=False)
            nuevaTarea.usuario = User.objects.get(username=nuevaTarea.encargado)
            nuevaTarea.proyecto = Proyecto.objects.get(id=id)
            nuevaTarea.save()
            return redirect('listaTarea' , id=id)

def editarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    usuario = User.objects.all()
    
    if request.method == 'POST':
        form = FormTarea(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('listaTarea', id=tarea.proyecto.id)
    
    # Si la solicitud no es un POST o el formulario no es válido, renderiza la página de edición nuevamente
    return render(request, 'editarTarea.html', {
        'form': FormTarea(instance=tarea),
        'usuario': usuario,
        'id': id,
    })
    
def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()   
    return redirect('listaTarea', id=tarea.proyecto.id) 

def listaRecurso(request, id):
    proyecto = Proyecto.objects.get(id=id)
    recurso = Recurso.objects.filter(proyecto=proyecto)
    return render(request, 'listaRecurso.html', {'recurso': recurso,'id':id})

def agregarRecurso(request, id):
    if request.method == 'GET':
        return render(request,'agregarRecurso.html', {
            'id':id,
            'form': FormRecurso,
        })
    else:
        form = FormRecurso(request.POST)
        if form.is_valid():
            nuevoRecurso = form.save(commit=False)
            nuevoRecurso.proyecto = Proyecto.objects.get(id=id)
            nuevoRecurso.save()
            return redirect('listaRecurso', id=id)
    
def editarRecurso(request, id):
    recurso = Recurso.objects.get(id=id)
    if request.method == 'POST':
        form = FormRecurso(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('listaRecurso', id=recurso.proyecto.id)
    return render(request, 'editarRecurso.html', {
        'form': FormRecurso(instance=recurso)
    }) 
    
def eliminarRecurso(request, id):
    recurso = Recurso.objects.get(id=id)
    recurso.delete()   
    return redirect('listaRecurso', id=recurso.proyecto.id) 

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
    tareas = Tarea.objects.filter(proyecto=proyecto)
    if request.method == 'GET':
        return render(request, 'proyecto.html', {
            'tareas': tareas,
            'proyecto': proyecto,
            'id': id,
            })
    return redirect(reverse('listaTarea' , args=[proyecto.id]))


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

def listaReporte(request, id):
    proyecto = Proyecto.objects.get(id=id)
    reportes = Reporte.objects.filter(proyecto=proyecto)
    return render(request, 'listaReporte.html', {'reportes': reportes,'id':id})
    

def crearReporte(request, id):    
    if request.method == 'GET':
        return render(request,'crearReporte.html', {
            'id':id,
            'form': FormReporte,
        })
    else:
        form = FormReporte(request.POST)
        if form.is_valid():
            nuevoReporte = form.save(commit=False)
            nuevoReporte.proyecto = Proyecto.objects.get(id=id)
            nuevoReporte.save()
            return redirect('listaReporte', id=id)

        
def editarReporte(request, id):
    reporte = Reporte.objects.get(id=id)
    if request.method == 'POST':
        form = FormReporte(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect('listaReporte', id=reporte.proyecto.id)
    return render(request, 'editarReporte.html', {
        'form': FormReporte(instance=reporte)
    }) 
    
def eliminarReporte(request, id):
    reporte = Reporte.objects.get(id=id)
    reporte.delete()   
    return redirect('listaReporte', id=reporte.proyecto.id) 
        
