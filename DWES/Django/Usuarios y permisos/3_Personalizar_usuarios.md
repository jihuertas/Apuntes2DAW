En Django, es posible personalizar el modelo de usuarios que viene de manera predeterminada en el framework. Para ello podremos usar la clase `AbstractUser`. Esto es útil si necesitamos añadir campos adicionales al modelo de usuario o modificar su comportamiento.

Veamos cómo podemos usar `AbstractUser`:

---

### 1. **Crea un modelo personalizado que herede de `AbstractUser`**
Definimos un modelo de usuario personalizado extendiendo de `AbstractUser`. Esto nos permite añadir nuevos campos o modificar los existentes.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Agrega campos adicionales
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
```

---

### 2. **Configura Django para usar tu modelo personalizado**
Debemos indicar en el archivo de configuración (`settings.py`) que estamos usando un modelo de usuario personalizado:

```python
AUTH_USER_MODEL = 'your_app_name.CustomUser'
```

Reemplaza `your_app_name` con el nombre de tu aplicación.

---

### 3. **Realiza las migraciones**
Después de crear el modelo, genera y aplica las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4. **Usar el modelo personalizado**
En lugar de importar directamente `User` desde `django.contrib.auth.models`, debes importar el modelo de usuario desde donde lo hayas definido. Por ejemplo:

```python
from your_app_name.models import CustomUser
```

---
### 5. **Actualiza formularios y administradores**
Si estás usando el panel de administración de Django, es necesario personalizar la forma en que el modelo de usuario se administra. Puedes hacerlo creando un administrador personalizado:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'birth_date')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
```

### Notas importantes
- Es recomendable definir el modelo de usuario personalizado al inicio del proyecto. Cambiarlo después de haber ejecutado migraciones puede ser complejo (siempre puedes borrar las migraciones y eliminar la base de datos).
- Al usar `AbstractUser`, heredas toda la funcionalidad del modelo de usuario predeterminado y puedes extenderlo según tus necesidades.
- Si necesitas una personalización más básica, puedes usar `AbstractBaseUser`, pero este requiere implementar manualmente más métodos y configuraciones.
