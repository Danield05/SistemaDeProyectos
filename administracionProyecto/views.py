from django.shortcuts import render, redirect
from .forms import FormTarea , FormRecurso, ProyectoForm, FormReporte
from .models import Tarea, Recurso, Proyecto, Reporte
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test



def es_administrador(user):
  return user.groups.filter(name="Administrador").exists()

administrador_requerido = user_passes_test(es_administrador)

def es_supervisor(user):
    return user.groups.filter(name="Supervisor").exists()

supervisor_requerido = user_passes_test(es_supervisor)

def es_administrador_o_supervisor(user):
    return user.groups.filter(name="Administrador").exists() or user.groups.filter(name="Supervisor").exists()

administrador_o_supervisor_requerido = user_passes_test(es_administrador_o_supervisor)

def es_inversor(user):
    return user.groups.filter(name="Inversor").exists()

inversor_requerido = user_passes_test(es_inversor)

def not_in_group(group):
    def in_group(user):
        if user.groups.filter(name=group).exists():
            return False
        return True
    return in_group

def es_empleado_formulador_proyectos(user):
    return user.groups.filter(name="Empleado Formulador de proyectos").exists()

formulador_requerido = user_passes_test(es_empleado_formulador_proyectos)

#todos menos el inversor
@login_required
@user_passes_test(not_in_group("Inversor"))
def listaTarea(request, id):
    proyecto = Proyecto.objects.get(id=id)
    tarea = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'listaTarea.html',{'id':id,'tarea': tarea})

#administrador y supervisor
@login_required
@administrador_o_supervisor_requerido
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

#supervisor y administrador
@login_required
@administrador_o_supervisor_requerido
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

#administrador y supervisor
@login_required
@administrador_o_supervisor_requerido
def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()   
    return redirect('listaTarea', id=tarea.proyecto.id) 

@login_required
@user_passes_test(not_in_group("Inversor"))
def listaRecurso(request, id):
    proyecto = Proyecto.objects.get(id=id)
    recurso = Recurso.objects.filter(proyecto=proyecto)
    return render(request, 'listaRecurso.html', {'id':id,'recurso': recurso})

@login_required
@administrador_requerido
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
        
@login_required
@administrador_requerido
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

@login_required
@administrador_requerido
def eliminarRecurso(request, id):
    recurso = Recurso.objects.get(id=id)
    recurso.delete()   
    return redirect('listaRecurso', id=recurso.proyecto.id) 

@login_required
def gestionar(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestionarProyecto.html', {'proyectos': proyectos})


@login_required
@user_passes_test(not_in_group("Inversor"))
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

@login_required
@user_passes_test(not_in_group("Inversor"))
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
    
@login_required
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

@login_required
@user_passes_test(not_in_group("Inversor"))
def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect(to='gestionar_proyecto')

@login_required
@administrador_requerido
def aprobarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        proyecto.aprobado = True
        proyecto.save()
        return redirect(reverse('proyecto', args=[proyecto.id]))
    return render(request, 'proyecto.html', {'proyecto': proyecto})

@login_required
def listaReporte(request, id):
    if request.user.groups.filter(name="Inversor").exists():
        reportes = Reporte.objects.filter(proyecto=id, tipo="financiero")
    else:
        reportes = Reporte.objects.filter(proyecto=id)
    
    return render(request, 'listaReporte.html',{'id':id,'reportes': reportes})
    
@login_required
def crearReporte(request, id):    
    if request.method == 'GET':
        return render(request,'crearReporte.html', {
            'id':id,
            'form': FormReporte,
            'es_inversor': request.user.groups.filter(name="Inversor").exists(),
        })
    else:
        form = FormReporte(request.POST)
        if form.is_valid():
            nuevoReporte = form.save(commit=False)
            nuevoReporte.proyecto = Proyecto.objects.get(id=id)
            nuevoReporte.save()
            return redirect('listaReporte', id=id)

@login_required
@user_passes_test(not_in_group("Inversor")) 
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

@login_required
@user_passes_test(not_in_group("Inversor")) 
def eliminarReporte(request, id):
    reporte = Reporte.objects.get(id=id)
    reporte.delete()   
    return redirect('listaReporte', id=reporte.proyecto.id) 
        
