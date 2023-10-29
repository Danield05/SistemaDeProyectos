from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'objetivo', 'prioridad', 'fecha_inicio', 'fecha_fin', 'presupuesto']