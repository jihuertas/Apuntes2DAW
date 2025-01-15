Veamos de qué forma podemos crear una página para que los usuarios se puedan registrar.

---

## **Crear una Página de Registro**

Django incluye el formulario `UserCreationForm` en `django.contrib.auth.forms`, que facilita la creación de usuarios. Solo necesitamos:

1. Configurar una vista.
2. Usar este formulario en la vista.
3. Crear una plantilla básica.

---

### **1. Configura la Vista de Registro**

Puedes usar una vista basada en clases (`CreateView`) para gestionar el formulario automáticamente.

#### Ejemplo:
```python
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')  # Redirige al login después del registro
```

---

### **2. Crea la Plantilla**

En la plantilla `registro.html`, renderiza el formulario de Django automáticamente.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro</title>
</head>
<body>
    <h2>Crear una cuenta</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Registrarse</button>
    </form>
</body>
</html>
```

---

### **3. Configura la URL**

En tu archivo `urls.py`, registra la vista para la página de registro.

```python
from django.urls import path
from .views import RegistroView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
]
```

---

### **4. Redirección Automática**

Después del registro, el usuario será redirigido automáticamente a la página de inicio de sesión (o donde tú configures en `success_url`).

---

### **Opciones de Personalización**

Si deseas agregar más campos, puedes extender `UserCreationForm` como en el ejemplo anterior, pero si solo necesitas lo básico, este método ya funciona perfectamente.

---
