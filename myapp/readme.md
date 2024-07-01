# Mi Proyecto Django

## Estructura

- `myproject/`: Carpeta principal del proyecto.
- `myapp/`: Aplicación Django.
    - `models.py`: Definición de modelos.
    - `views.py`: Definición de vistas.
    - `forms.py`: Definición de formularios.
    - `templates/`: Templates HTML.

## Orden de Prueba

1. Crear y migrar modelos: `python manage.py makemigrations`, `python manage.py migrate`.
2. Ejecutar servidor de desarrollo: `python manage.py runserver`.
3. Probar funcionalidades:
   - Agregar categoría: `/agregar_categoria/`.
   - Agregar producto: `/agregar_producto/`.
   - Agregar cliente: `/agregar_cliente/`.
   - Buscar producto: `/buscar/?q=`.
