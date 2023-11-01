from django.urls import include, path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('home/')),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
