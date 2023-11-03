from django.contrib import admin
from .models import Tarea, Recurso, Proyecto, Reporte
# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Recurso)
admin.site.register(Reporte)