from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes':clientes})

def create_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        email = request.POST['email']
        telefono = request.POST['telefono']
        cliente = Cliente(nombre=nombre, direccion=direccion, email=email, telefono=telefono)
        cliente.save()
    return redirect('/clientes/')
    #return render(request, 'create_cliente.html')

def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/clientes/')

