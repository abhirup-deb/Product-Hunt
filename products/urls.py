from django.urls import path,include
from . import views

urlpatterns = [
    path( 'products/Create', views.Create, name='Create'),
    path('<int:product_id>', views.Detail, name="Detail"),
    path('<int:product_id>/upvote', views.upvote, name="upvote"),
]
