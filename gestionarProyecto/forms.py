from django import forms
from django.contrib.auth.models import User
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, required=True, label='Nombre del Proyecto')
    objetivo = forms.CharField(max_length=200, required=True, label='Objetivo')
    
    PRIORIDAD_CHOICES = (
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    )
    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completado', 'Completado'),
    )
    prioridad = forms.ChoiceField(choices=PRIORIDAD_CHOICES, required=True, label='Prioridad')
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, required=True, label='Estado')
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Fecha de Inicio')
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Fecha de Fin')
    presupuesto = forms.DecimalField(required=True, label='Presupuesto')
    #encargadoProyecto = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label='Encargado del Proyecto')
    class Meta:
        model = Proyecto
        fields = ['nombre', 'objetivo', 'prioridad', 'fecha_inicio', 'fecha_fin', 'presupuesto', 'encargado']
        

        