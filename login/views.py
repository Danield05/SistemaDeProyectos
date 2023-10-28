from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')


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
                user = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
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
    return redirect('home')


def signin(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
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
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario y/o contraseña incorrectos'
            })

    return render(request, 'signin.html', {
        'form': AuthenticationForm()
    })
        

    
