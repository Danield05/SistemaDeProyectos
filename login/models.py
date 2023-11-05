# from django.contrib.auth.models import Group

# #Crear grupos/roles
# admin_group, created = Group.objects.get_or_create(name='Administrador')
# sup_group, created = Group.objects.get_or_create(name='Supervisor')
# emp_group, created = Group.objects.get_or_create(name='Empleado Formulador de proyectos')
# inv_group, created = Group.objects.get_or_create(name='Inversor')
# #documentacion
# #https://vegibit.com/how-to-create-and-use-django-groups-for-user-management/

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    dui = models.CharField(max_length=12, blank=True)
    pais = models.CharField(max_length=30, blank=True)
    nit = models.CharField(max_length=20, blank=True)
    departamento = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=30, blank=True)
 

#this method to generate profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#this method to update profile when user is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()