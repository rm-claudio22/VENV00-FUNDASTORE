from django.db import models
from django.conf import settings
from pathlib import Path, os

from django.utils.translation import gettext_lazy as _

# Create your models here.
class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=255)
    cat_itbms  = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.cat_nombre

class Productos(models.Model):
    class Moneda(models.TextChoices):
        USD = 'USD',_('DÓLAR ESTADOUNIDENSE')
        EUR = 'EUR',_('EURO')
        PAB = 'PAB',_('BALBOA PANAMEÑO')

    pro_id = models.AutoField(primary_key=True)
    pro_nombre = models.CharField(max_length=255)
    pro_precio = models.DecimalField(decimal_places=2, max_digits=8)
    pro_moneda = models.CharField(max_length=3,choices=Moneda.choices,default=Moneda.USD)
    pro_stock  = models.IntegerField()
    pro_descripcion = models.TextField(null=True)
    pro_categoria   = models.ForeignKey(to=Categoria, on_delete=models.CASCADE,null=True)
    pro_imagen =models.ImageField(upload_to='PRODUCTO', max_length=255, default='default.png',blank=True)
    def __str__(self):
        return self.pro_nombre

