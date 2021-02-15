from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    class Categoria(models.TextChoices):
        RECETAS = 'R',_('RECETAS')
        NOTICIAS = 'N',_('NOTICIAS')

    blg_id     = models.AutoField(primary_key=True)
    blg_tipo   = models.CharField(max_length=1,choices=Categoria.choices)
    blg_titulo = models.CharField(max_length=128)
    blg_descripcion = models.TextField(default="Algo de texto aqui")
    blg_banner = models.ImageField(upload_to='blog/banners', max_length=255)
    blg_mini   = models.ImageField(upload_to='blog/banners', max_length=255, null=True)
    blg_video  = models.URLField()
    blg_post   = HTMLField()
    blg_fecha_post = models.DateTimeField(auto_now_add=True)
    blg_fecha_act  = models.DateTimeField(auto_now=True)
    