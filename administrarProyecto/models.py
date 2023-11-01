from django.db import models
from django.contrib.auth.models import User
from gestionarProyecto.models import Proyecto


# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50, blank=False, null=False, default='Pendiente')
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    encargado = models.CharField(max_length=50, blank=False, null=False, default='no asignado')
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' - ' + self.estado
    
class Recurso(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    disponibilidad = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre