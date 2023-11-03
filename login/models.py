from django.contrib.auth.models import Group

# Crear grupos/roles
admin_group, created = Group.objects.get_or_create(name='Administrador')
sup_group, created = Group.objects.get_or_create(name='Supervisor')
emp_group, created = Group.objects.get_or_create(name='Empleado Formulador de proyectos')
inv_group, created = Group.objects.get_or_create(name='Inversor')
#documentacion
#https://vegibit.com/how-to-create-and-use-django-groups-for-user-management/
