from django.forms import ModelForm 
from .models import Tarea
from .models import Recurso
from .models import Proyecto 
from .models import Reporte
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
      
class FormRecurso(ModelForm):
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    descripcion = forms.CharField(max_length=200, required=True, label='Descripción')
    disponibilidad = forms.BooleanField(initial=True, required=False, label='Disponibilidad')
    cantidad = forms.IntegerField(required=True, label='Cantidad')

    class Meta:
        model = Recurso
        fields = ['nombre', 'descripcion', 'disponibilidad', 'cantidad']
      
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
        
class FormReporte(ModelForm):
    TIPO_CHOICES = (
        ('general', 'Reporte General'),
        ('financiero', 'Reporte Financiero'),
    )
    titulo = forms.CharField(max_length=50, required=True, label='Titulo')
    descripcion = forms.CharField(max_length=500, required=True, label='Descripción')
    tipo = forms.ChoiceField(choices=TIPO_CHOICES, required=True, label='Tipo')

    class Meta:
        model = Reporte
        fields = ['titulo', 'descripcion', 'tipo']
              