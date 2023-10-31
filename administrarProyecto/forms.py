from django.forms import ModelForm 
from .models import Tarea
from django import forms
from django.contrib.auth.models import User


class FormTarea(ModelForm):
    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    )

    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    descripcion = forms.CharField(max_length=200, required=True, label='Descripción')
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, required=True, label='Estado')
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Fecha Inicio')
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Fecha Fin')

    encargado = forms.ChoiceField(
        choices=[('', 'Seleccione un encargado')] + [(usuario.username, usuario.username) for usuario in User.objects.all()],
        required=False,  # No requerido porque tienes la opción "Seleccione un encargado"
        label='Encargado'
    )

    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado', 'encargado']