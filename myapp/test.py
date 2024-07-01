from django.test import TestCase
from .models import Categoria, Producto, Cliente

class ModelosTestCase(TestCase):
    def setUp(self):
        Categoria.objects.create(nombre="Electrónicos")
        Producto.objects.create(nombre="Smartphone", categoria_id=1, precio=599.99)
        Cliente.objects.create(nombre="Juan Pérez", direccion="Calle 123", email="juan@example.com")

    def test_modelos_creados_correctamente(self):
        categoria = Categoria.objects.get(id=1)
        producto = Producto.objects.get(id=1)
        cliente = Cliente.objects.get(id=1)
        
        self.assertEqual(categoria.nombre, "Electrónicos")
        self.assertEqual(producto.nombre, "Smartphone")
        self.assertEqual(cliente.nombre, "Juan Pérez")

    # Agrega más pruebas según sea necesario
