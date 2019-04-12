from django.urls import path,include
from . import views

urlpatterns = [
    path( 'accounts/Signup', views.Signup, name='Signup'),
    path( 'accounts/Login', views.Login, name='Login'),
    #path( 'accounts/Logout', views.Logout, name='Logout'),
]
