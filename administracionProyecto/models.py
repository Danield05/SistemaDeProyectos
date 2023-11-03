from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Proyecto(models.Model):
    aprobado=models.BooleanField(null=False, blank=False, default=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    objetivo = models.CharField(max_length=255, blank=False, null=False)
    prioridad = models.CharField(max_length=15, blank=False, null=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)
    estado = models.CharField(max_length=15,null=False, blank=False, default='Pendiente')
    encargadoProyecto = models.CharField(max_length=50, null=False, blank=False, default='no asignado')
    encargado = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

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
    
class Reporte(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=False, null=False)
    importante =  models.BooleanField(default=False)
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo