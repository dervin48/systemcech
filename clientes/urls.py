from django import views
from django.urls import path
from .views import clientes, create_cliente, delete_cliente

urlpatterns = [
path('', clientes, name="clientes"),
path('nuevo/', create_cliente, name="create_cliente"),
path('delete_cliente/<int:id>/', delete_cliente, name="delete_cliente"),



]