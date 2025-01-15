Django integra unas URLs predeterminadas del sistema de autenticación para realizar login y logout. Veamos cómo podelos usarlas y personalizarlas.

---

## 1. Configura las URLs en `urls.py`
Edita el archivo `urls.py` principal de tu proyecto para incluir las URLs del sistema de autenticación:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs predeterminadas de Django
]
```

---

## 2. Personaliza las plantillas
Crea un directorio llamado `templates` en la raíz del proyecto o dentro de tu aplicación. Luego, crea una subcarpeta `registration` dentro de `templates`.

```plaintext
mi_proyecto/
    templates/
        registration/
            login.html
            logged_out.html
```

### Plantilla personalizada para login (`templates/registration/login.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar sesión</title>
</head>
<body>
    <h1>Iniciar sesión</h1>
    {% if form.errors %}
        <p>Por favor, corrige los siguientes errores:</p>
        {{ form.errors }}
    {% endif %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Iniciar sesión</button>
    </form>
    <p>¿No tienes una cuenta? <a href="{% url 'admin:index' %}">Contacta al administrador</a>.</p>
</body>
</html>
```

### Plantilla personalizada para logout (`templates/registration/logged_out.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cerrar sesión</title>
</head>
<body>
    <h1>Sesión cerrada</h1>
    <p>Has cerrado sesión correctamente. <a href="{% url 'login' %}">Iniciar sesión de nuevo</a>.</p>
</body>
</html>
```
IMPORTANTE: Para que funcione el logout NO se puede usar GET. Por ello, se debe usar:
```html
<form action="{% url 'logout' %}" method="post">
  {% csrf_token %} 
  <button type="submit" class="">Cerrar Sesión</button>
</form>
```

---

## 3. Configura las vistas personalizadas
Django usa vistas genéricas para manejar el login y logout. Puedes sobrescribir su comportamiento configurando las opciones en `settings.py`:

```python
# Redirigir después de iniciar sesión
LOGIN_REDIRECT_URL = '/'  # Cambia esto a la URL que desees

# Redirigir después de cerrar sesión
LOGOUT_REDIRECT_URL = '/accounts/login/'  # Cambia esto si lo necesitas
```

---

## 4. Personalizar contenido en función de si está o no autenticado
Si deseas mostrar contenido adicional o diferente a los usuarios autenticados, puedes usar la condición {% if user.is_authenticated %} en cualquier parte de las plantillas.
```html
{% if user.is_authenticated %}
    <p>¡Bienvenido de nuevo, {{ user.first_name }}!</p>
{% else %}
    <p>Por favor, <a href="{% url 'login' %}">inicia sesión</a> para acceder a más funciones.</p>
{% endif %}


```

Accede a `/accounts/login/` para ver tu formulario de inicio de sesión personalizado y a `/accounts/logout/` para probar el cierre de sesión.
