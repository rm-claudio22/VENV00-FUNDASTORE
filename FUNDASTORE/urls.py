"""FUNDASTORE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .APPS.PRODUCTOS.views import *
from .APPS.PRINCIPAL.views import *
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #PRINCIPAL
    path('',inicio),
    path('contactenos',ver_contactenos, name='pricipal-contactenos'),

    path('blog/recetas',recetas, name='pricipal-blog-recetas'),
    path('blog/recetas/<int:id>',verReceta, name='pricipal-blog-recetas-detalle'),

    path('ListarProductos',ListarProductos, name='ListarProductos'),
    path('AgregarProductos',agregarProductos, name='AgregarProductos'),
    path('LeerProductos/<int:id>',leerProducto, name='LeerProductos'),
    path('EditarProductos/<int:id>',editarProducto, name='EditarProductos'),
    path('EliminarProductos/<int:id>',eliminarProducto, name='EliminarProductos'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

