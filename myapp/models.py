from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'myapp'  

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'myapp'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        app_label = 'myapp'
