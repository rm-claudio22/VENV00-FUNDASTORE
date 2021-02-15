from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
from .forms import *

# Create your views here.


def inicio(request):
    return render(request, 'PRINCIPAL/index.html')

def ver_contactenos(request):
    if request.method == 'POST':
        formulario = FormularioContactenos(request.POST)
        subject = 'SOLICITUD DE CONTACTENOS - ' + str(formulario['nombre'].value())
        message = 'INFORMACION DE CONTACTO\n'
        message = message + '\nNOMBRE: ' +  str(formulario['nombre'].value())
        message = message + '\nEMAIL: '  +  str(formulario['email'].value())
        message = message + '\nTELEFONO: '  +  str(formulario['telefono'].value())
        message = message + '\n\nCONSULTA \n'  +  str(formulario['mensaje'].value())
        recepient = [str(formulario['email'].value())]
        send_mail(subject, message, None, recepient, fail_silently = False)
    else:
        formulario = FormularioContactenos()
    contexto = {'formulario': formulario}
    return render(request,'PRINCIPAL/contactenos.html',contexto)

def recetas(request):
    blogs = Blog.objects.filter(blg_tipo='R')
    contexto = {"recetas":blogs}
    return render(request, 'PRINCIPAL/blog/recetas/index.html',context=contexto)

def verReceta(request, id):
    post = Blog.objects.get(blg_id=id)
    contexto = {'receta':post}
    return render(request, 'PRINCIPAL/blog/recetas/detalle.html', contexto)