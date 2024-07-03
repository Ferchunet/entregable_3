from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    # Ensure 'direccion' is a field here if you want to include it in the form
    nombre = models.CharField(max_length=100)
    # Other fields
    direccion = models.CharField(max_length=200)  # Add this line if 'direccion' is supposed to be part of the model

    def __str__(self):
        return self.nombre