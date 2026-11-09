# Bloque 8. Panel de administración de Django

## Objetivos

- Comprender para qué sirve Django Admin y cómo se relaciona con los modelos.
- Crear un superusuario y acceder al panel de administración.
- Registrar modelos y personalizar listados, filtros y búsquedas.
- Gestionar registros y relaciones desde la interfaz administrativa.

## 1. ¿Qué es Django Admin?

Django incluye un panel de administración generado a partir de los modelos registrados. Permite a usuarios autorizados **crear, consultar, modificar y eliminar** registros mediante una interfaz web, sin programar formularios y vistas CRUD desde cero. Está pensado principalmente para gestión interna; no sustituye necesariamente a la interfaz pública de una aplicación.

El panel utiliza el ORM y respeta los permisos de los usuarios. Para utilizarlo, comprueba que `django.contrib.admin` esté en `INSTALLED_APPS` y que la ruta de administración aparezca en `biblioteca/urls.py`:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```

## 2. Crear un superusuario y acceder

Desde la carpeta donde se encuentra `manage.py`:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre `http://127.0.0.1:8000/admin/` e inicia sesión con el usuario creado. **No incluyas contraseñas en el repositorio.**

## 3. Registrar modelos

En `catalogo/admin.py`:

```python
from django.contrib import admin
from .models import Autor, Editorial, Libro, Prestamo

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Prestamo)
```

Los modelos registrados aparecen en el panel y pueden administrarse según los permisos del usuario. Si alguno ya está registrado mediante `@admin.register`, **no lo registres por segunda vez**.

## 4. Personalizar la administración de libros

Sustituye el registro simple de `Libro` por una clase `ModelAdmin`:

```python
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "isbn", "precio", "disponible", "editorial")
    list_filter = ("disponible", "editorial")
    search_fields = ("titulo", "isbn", "autores__nombre")
    ordering = ("titulo",)
    list_per_page = 20
    filter_horizontal = ("autores",)
```

Este ejemplo presupone que en el bloque 6 se añadieron `editorial` y `autores` al modelo `Libro`. **Asegúrate de que el nombre de los campos coincide con tu código**.

| Opción | Efecto |
|---|---|
| `list_display` | Columnas visibles en el listado |
| `list_filter` | Filtros laterales |
| `search_fields` | Campos consultados desde el buscador |
| `ordering` | Orden inicial del listado |
| `list_per_page` | Número de registros por página |
| `filter_horizontal` | Selector más cómodo para relaciones muchos a muchos |

## 5. Personalizar otros modelos

```python
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellidos", "nacionalidad")
    search_fields = ("nombre", "apellidos")


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa")
    list_filter = ("activa",)
    search_fields = ("nombre",)
```

Si empleas estos decoradores, elimina los registros simples correspondientes del apartado 3. Para `Prestamo`, comienza con `admin.site.register(Prestamo)` y revisa los nombres de los campos antes de añadir opciones de listado.

## 6. Usuarios, permisos e integridad

Un superusuario tiene acceso amplio al panel. Otros usuarios necesitan `is_staff=True` para acceder y permisos adecuados sobre cada modelo (añadir, cambiar, eliminar o ver). No todos los usuarios autenticados pueden administrar registros.

El panel aplica validaciones de formularios, pero **no sustituye las restricciones de la base de datos ni las transacciones** desarrolladas en el bloque 7. Por ejemplo, una regla de negocio compleja sobre préstamos no queda garantizada solo por mostrar un campo `disponible` en Admin.

## Actividad 8. Administración de la biblioteca 
**Enunciado:** Prepara el panel de administración para gestionar los datos de la biblioteca.

1. Crea un superusuario y accede al panel.
2. Registra los modelos `Autor`, `Editorial`, `Libro` y `Prestamo`.
3. Personaliza el listado de libros para mostrar título, ISBN, precio, disponibilidad y editorial.
4. Añade filtros por disponibilidad y editorial.
5. Permite buscar libros por título, ISBN y nombre del autor.
6. Configura un selector adecuado para los autores de cada libro.
7. Personaliza los listados de autores y editoriales.
8. Crea una editorial, dos autores y tres libros desde Admin; modifica un registro y elimina otro que no tenga dependencias protegidas.
9. Crea un usuario de personal sin privilegios de superusuario y comprueba la diferencia entre permisos de lectura y modificación.

**Entrega:** `admin.py` y capturas de los listados, filtros, búsqueda y permisos probados.

**Preguntas:** ¿Qué aporta `ModelAdmin`? ¿Por qué no debemos utilizar siempre una cuenta de superusuario? ¿Qué diferencia hay entre una validación del formulario y una restricción de base de datos?



**Siguiente bloque:** configuración de Django con diferentes gestores de bases de datos.
