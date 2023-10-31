from django import forms
from django.contrib.auth.models import User
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'objetivo', 'prioridad', 'fecha_inicio', 'fecha_fin', 'presupuesto', 'encargadoProyecto']