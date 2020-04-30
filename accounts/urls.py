
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Dashboard'),
    path('products/', views.products, name='Product'),
    path('customer/<str:pk>/', views.customer, name='Customer'),
]
