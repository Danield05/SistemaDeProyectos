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
        return self.nombre + ' ' + self.estado


