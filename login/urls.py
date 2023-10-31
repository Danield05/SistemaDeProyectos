from django.urls import include, path
from . import views
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('', include(tf_urls))
]
