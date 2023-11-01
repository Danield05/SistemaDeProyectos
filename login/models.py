# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     # Campos adicionales
#     first_name2 = models.CharField(max_length=30)
#     last_name2 = models.CharField(max_length=30)

#     # Definir opciones para el campo "Rol"
#     ROL_CHOICES = (
#         ('1', 'Formulador de Proyectos'),
#         ('2', 'Supervisor'),
#         ('3', 'Inversionista'),
#     )
#     rol2 = models.CharField(max_length=1, choices=ROL_CHOICES)

#     def __str__(self):
#         return self.username

# def CustomUser( username, email, password, first_name, last_name, rol):
#         user.set_password(password),
#         user.username = username,
#         user.is_staff = True
#         user.is_superuser = False
#         user.save(using=self._db)
#         return user 

# class UserProfile(AbstractBaseUser, PermissionsMixin):

#     alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
#     username    = models.CharField(unique=True, max_length=20, validators=[alphanumeric])
#     email       = models.EmailField(verbose_name='email address', unique=True, max_length=244)
#     first_name  = models.CharField(max_length=30, null=True, blank=True)
#     last_name   = models.CharField(max_length=50, null=True, blank=True)
#     is_active   = models.BooleanField(default=True, null=False)
#     is_staff    = models.BooleanField(default=False, null=False)