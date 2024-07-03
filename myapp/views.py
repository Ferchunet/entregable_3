from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .models import Categoria, Producto, Cliente
from .models import Producto  # Asegúrate de importar el modelo Producto adecuadamente
from django.shortcuts import render
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def buscar(request):
    resultados = []
    query = request.GET.get('q')
    if query:
        resultados = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'buscar.html', {'resultados': resultados})

def inicio(request):
    return render(request, 'inicio.html')
