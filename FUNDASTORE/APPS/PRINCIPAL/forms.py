from django import forms

class FormularioContactenos(forms.Form):
    nombre = forms.CharField(max_length=128)
    email   = forms.EmailField()
    telefono = forms.CharField(max_length=64, label='Teléfono')
    mensaje = forms.CharField(widget=forms.Textarea)
