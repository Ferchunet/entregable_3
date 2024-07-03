# forms.py
from django import forms
from .models import Categoria, Producto, Cliente

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre']  # Add other fields as needed, and remove 'direccion' if it is not part of the model
