from django.urls import path,include
from . import views

urlpatterns = [
    path( 'products/Create', views.Create, name='Create'), 
]
