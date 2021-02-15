from django import forms
from .models import Productos

class FormularioProductos(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        labels = {'pro_nombre':'NOMBRE'}