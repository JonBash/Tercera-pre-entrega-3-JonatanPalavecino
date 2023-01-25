from django import forms


class RecetaFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    bio = forms.TextInput()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    precio = forms.IntegerField()

class ClienteFormulario(forms.Form):
    apellido = forms.CharField(max_length=64)
    nombre = forms.CharField(max_length=64)
    