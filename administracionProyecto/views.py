from django.shortcuts import render, redirect
from .forms import FormTarea , FormRecurso, ProyectoForm, FormReporte
from .models import Tarea, Recurso, Proyecto, Reporte
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
#Lista tarea
def listaTarea(request, id):
    proyecto = Proyecto.objects.get(id=id)
    tarea = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'listaTarea.html',{'id':id,'tarea': tarea})
#Crear tarea
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


#Editar tarea
def editarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    usuario = User.objects.all()
    
    if request.method == 'POST':
        # Obtén los datos del formulario personalizado
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('id_estado')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        encargado = request.POST.get('id_encargado')
        # Actualiza la tarea con los nuevos datos
        tarea.nombre = nombre
        tarea.descripcion = descripcion
        tarea.estado = estado
        tarea.fecha_inicio = fecha_inicio
        tarea.fecha_fin = fecha_fin
        tarea.encargado = encargado
        tarea.save()

        return redirect('listaTarea', id=tarea.proyecto.id)

    return render(request, 'editarTarea.html', {
        'tarea': tarea,
        'usuario': usuario,
        'id': id,
    })

  #Eliminar tarea  
def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()   
    return redirect('listaTarea', id=tarea.proyecto.id) 
#Lista recurso
def listaRecurso(request, id):
    proyecto = Proyecto.objects.get(id=id)
    recurso = Recurso.objects.filter(proyecto=proyecto)
    return render(request, 'listaRecurso.html', {
        'id':id,
        'recurso': recurso,
        'es_administrador': request.user.groups.filter(name="Administrador").exists(),
        })

#Agregar recurso
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
    
    


#editar recurso
def editarRecurso(request, id):
    recurso = Recurso.objects.get(id=id)

    if request.method == 'POST':
        # Obtén los datos del formulario directamente
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        disponibilidad = request.POST.get('disponibilidad')
        cantidad = request.POST.get('cantidad')

        # Actualiza el recurso con los nuevos datos
        recurso.nombre = nombre
        recurso.descripcion = descripcion
        recurso.disponibilidad = disponibilidad
        recurso.cantidad = cantidad
        recurso.save()

        return redirect('listaRecurso', id=recurso.proyecto.id)

    return render(request, 'editarRecurso.html', {
        'recurso': recurso,
        'id': id,
    })

    #eliminar recurso
def eliminarRecurso(request, id):
    recurso = Recurso.objects.get(id=id)
    recurso.delete()   
    return redirect('listaRecurso', id=recurso.proyecto.id) 
#Gestionar recurso
def gestionar(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestionarProyecto.html', {
        'proyectos': proyectos,
        'es_inversor': request.user.groups.filter(name="Inversor").exists(),
    })

#Crear proyecto
def crearProyecto(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        proyecto = Proyecto.objects.all()
        tipos_prioridad = ProyectoForm.PRIORIDAD_CHOICES
        tipos_prioridad = [tipo[0] for tipo in tipos_prioridad]
        # haz lo mismo para que los tipos de prioridad para los tipos de estado en una sola linea
        tipos_estados = ProyectoForm.ESTADO_CHOICES
        tipos_estados = [tipo[0] for tipo in tipos_estados]
        encargado= User.objects.all()
        

        return render(request,'crearProyecto.html', {
            'usuarios': usuarios,
            'proyecto': proyecto,
            'form': ProyectoForm,
            'tipos_prioridad': tipos_prioridad,
            'tipos_estados': tipos_estados,
            'encargado': encargado,
            
        })
    else:
        form = ProyectoForm(request.POST)
        
        if form.is_valid():
            nuevoProyecto = form.save(commit=False)
            nuevoProyecto.estado =request.POST.get('estado')
            nuevoProyecto.usuario = User.objects.get(username=nuevoProyecto.encargado)
            nuevoProyecto.save()
        return redirect('gestionar_proyecto') 
  
 # Editar proyecto
def editarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    usuarios = User.objects.all()
    # Define las opciones de Estado manualmente
    estado_choices = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completado', 'Completado'),
    ]

    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST.get('nombre')
        objetivo = request.POST.get('objetivo')
        prioridad = request.POST.get('prioridad')
        estado = request.POST.get('estado')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        presupuesto = request.POST.get('presupuesto')
        encargado = request.POST.get('id_encargado')
        

        # Actualiza el proyecto con los nuevos datos
        proyecto.nombre = nombre
        proyecto.objetivo = objetivo
        proyecto.prioridad = prioridad
        proyecto.estado = estado
        proyecto.fecha_inicio = fecha_inicio
        proyecto.fecha_fin = fecha_fin
        proyecto.presupuesto = presupuesto
        proyecto.encargado = encargado
        proyecto.save()

        return redirect('gestionar_proyecto')
    else:
        print(proyecto.encargado)
        return render(request, 'editarProyecto.html', {
        'proyecto': proyecto,
        'estado_choices': estado_choices,
        'usuarios': usuarios,
        'id': id,
    })

# Ver proyecto
def proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    if request.method == 'GET':
        return render(request, 'proyecto.html', {
            'tareas': tareas,
            'proyecto': proyecto,
            'id': id,
            'es_administrador': request.user.groups.filter(name="Administrador").exists(),
            'es_inversor': request.user.groups.filter(name="Inversor").exists(),
        })
    return redirect(reverse('listaTarea' , args=[proyecto.id]))

# Eliminar proyecto
def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect(to='gestionar_proyecto')
# Aprobar proyecto
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
    
    return render(request, 'listaReporte.html',{
        'id':id,
        'reportes': reportes,
        'es_inversor': request.user.groups.filter(name="Inversor").exists(),
    })
    
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
        
