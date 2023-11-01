from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.views.generic import View, UpdateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import authenticate, login as auth_login
from django_otp.forms import OTPAuthenticationForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from login.tokens import account_activation_token
from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.core.mail import EmailMessage
from django_otp import match_token
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def create_group_roles(dato):
    if dato =='0':
            rol= Group.objects.get(name='Administrador')
    elif dato == '1':  
            rol= Group.objects.get(name='Empleado Formulador de proyectos')
    elif dato=='2':
            rol= Group.objects.get(name='Supervisor')
    else:
            rol= Group.objects.get(name='Inversor')
    return rol

def create_employee(request):
    # Create a User
    user = User.objects.create_user(
        username=request.POST['username'],
        email=request.POST['email'],
        password=request.POST['password1'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
    )
    
    return  user


@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')

#signin

def get_user_totp_device(self,user, confirmed=None):
        devices = devices_for_user(user, confirmed=confirmed)
        for device in devices:
            if isinstance(device, TOTPDevice):
                return device
            
  #Registrarse          
@login_required()
def signup(request):
    
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                def get_user_totp_device(user, confirmed=None):
                    devices = devices_for_user(user, confirmed=confirmed)
                    for device in devices:
                        if isinstance(device, TOTPDevice):
                            return device

                if request.method == 'POST':

                    
                    user = create_employee(request)
                    group = create_group_roles(request.POST['rol'])   
                    user.groups.add(group)
                    user.save()

                    device = get_user_totp_device(user)
                    if not device:
                        device = user.totpdevice_set.create(confirmed=True)
                        # print(device.config_url)  # Imprime la URL del código QR por consola
                    current_site = get_current_site(request)
                    mail_subject = 'DATOS DE ACCESO'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'qr_code': device.config_url,
                    'contraseña': request.POST['password1'],
                    'rol' : request.POST['rol'],
                })
                to_email = request.POST['email']
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.content_subtype = "html"
                email.send()

                
                #login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            'error': 'Contraseñas no coinciden'
        })


@login_required()
def signout(request):
    logout(request)
    return redirect('/signin')

#signin
def signin(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        otp_token = request.POST['otp_token']
        user = None
        # Intenta autenticar al usuario primero por correo electrónico
        try:
            user = User.objects.get(email=username_or_email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            pass
        if user is None:
            # Si no se encuentra por correo electrónico, intenta autenticar por nombre de usuario
            user = authenticate(request, username=username_or_email, password=password)
        if user is not None:
            
            device_match = match_token(user=user, token=otp_token)
            if device_match is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                return  render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Token verficacion a 2 pasos incorrecto'
            })
        else:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario y/o contraseña incorrectos'
            })

    return render(request, 'signin.html', {
        'form': AuthenticationForm()
    })
        


  



