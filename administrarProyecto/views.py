from django.shortcuts import render, redirect
from .forms import FormTarea 
from .models import Tarea
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

