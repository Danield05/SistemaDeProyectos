from django.forms import ModelForm 
from .models import Tarea


class FormTarea(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado', 'encargado']
