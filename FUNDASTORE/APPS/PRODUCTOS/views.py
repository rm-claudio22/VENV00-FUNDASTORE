from django.shortcuts import render, redirect
from .models import Productos
from .forms import FormularioProductos
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def ListarProductos(request):
    prod = Productos.objects.all()
    contexto = {"productos":prod}
    return render(request, 'ListarProductos.html', context=contexto)

def agregarProductos(request):
    request.accion = 'C'
    if request.method == 'POST':
        form = FormularioProductos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ListarProductos')
    else:
        form = FormularioProductos()
        
    contexto = {"formulario":form}
    
    return render(request, 'AgregarProductos.html', contexto)

def leerProducto(request, id):
    request.accion = 'R'
    producto = Productos.objects.get(pro_id = id)
    formulario = FormularioProductos(instance=producto)
    contexto = {'formulario':formulario}
    return render(request, 'AgregarProductos.html', contexto)

def editarProducto(request, id):
    request.accion = 'U'
    producto = Productos.objects.get(pro_id = id)
    if request.method == 'POST':
        formulario = FormularioProductos(request.POST,request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('ListarProductos')
    else:
        formulario = FormularioProductos(instance=producto)
    contexto = {'formulario':formulario}
    return render(request, 'AgregarProductos.html', contexto)

def eliminarProducto(request, id):
    producto = Productos.objects.get(pro_id = id)
    producto.delete()
    return redirect('ListarProductos')
