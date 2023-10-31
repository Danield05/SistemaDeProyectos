from django.shortcuts import render, redirect
from .forms import FormTarea 
from .models import Tarea
from django.contrib.auth.models import User
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
    
    