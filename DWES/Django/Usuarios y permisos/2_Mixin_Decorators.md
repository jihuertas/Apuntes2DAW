### **Uso Básico de Mixins y Decoradores para Gestionar Permisos en Django**

En Django, los **mixins** y **decoradores** son herramientas útiles para controlar los permisos de acceso a vistas y recursos. Veamos cómo y cuándo se deben usar:

---

## **1. Mixins para Gestionar Permisos**

Los mixins son clases que puedes incluir en tus vistas basadas en clases (CBV, por sus siglas en inglés) para añadir funcionalidades específicas, como verificar permisos.

### Ejemplo con `LoginRequiredMixin`
Un uso común es asegurarte de que un usuario esté autenticado antes de acceder a una vista:

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Articulo

class ArticuloListView(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = 'articulos.html'
```

- **¿Qué hace?**
  - Redirige automáticamente al usuario a la página de inicio de sesión si no está autenticado.
  - Por defecto, busca la URL definida en `LOGIN_URL` en `settings.py`.

---

### Otros Mixins Útiles
- **`PermissionRequiredMixin`:** Verifica que el usuario tenga un permiso específico.
  ```python
  from django.contrib.auth.mixins import PermissionRequiredMixin

  class ArticuloDetailView(PermissionRequiredMixin, ListView):
      model = Articulo
      template_name = 'detalle_articulo.html'
      permission_required = 'app_name.view_articulo'
  ```
  - `permission_required`: Especifica el permiso necesario para acceder a la vista.

- **`UserPassesTestMixin`:** Permite definir una condición personalizada para otorgar acceso.
  ```python
  from django.contrib.auth.mixins import UserPassesTestMixin

  class SoloAdminsView(UserPassesTestMixin, ListView):
      model = Articulo
      template_name = 'admin_view.html'

      def test_func(self):
          return self.request.user.is_staff
  ```

---

## **2. Decoradores para Gestionar Permisos**

Los decoradores son funciones que modifican el comportamiento de otras funciones o métodos. Son más comunes en vistas basadas en funciones (FBV, por sus siglas en inglés).

### Ejemplo con `@login_required`
Verifica que el usuario esté autenticado antes de ejecutar la vista:

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def lista_articulos(request):
    return render(request, 'articulos.html')
```

- **¿Qué hace?**
  - Redirige al usuario a la página de inicio de sesión si no está autenticado.

---

### Otros Decoradores Útiles

- **`@permission_required`:** Verifica que el usuario tenga un permiso específico.
  ```python
  from django.contrib.auth.decorators import permission_required

  @permission_required('app_name.view_articulo')
  def detalle_articulo(request, id):
      # Lógica de la vista
      return render(request, 'detalle_articulo.html')
  ```

- **`@user_passes_test`:** Permite definir una condición personalizada.
  ```python
  from django.contrib.auth.decorators import user_passes_test

  def es_admin(user):
      return user.is_staff

  @user_passes_test(es_admin)
  def vista_admin(request):
      return render(request, 'admin_view.html')
  ```

---

## **3. Cuándo Usar Mixins o Decoradores**

- Usa **mixins** si trabajas con vistas basadas en clases (CBV). Son más reutilizables y se integran bien con la herencia de clases.
- Usa **decoradores** si trabajas con vistas basadas en funciones (FBV). Son más simples y directos.

---

## **4. Personalización**

Si necesitas reglas de permisos complejas, puedes crear tus propios mixins o decoradores. Por ejemplo:

### Mixin Personalizado
```python
from django.contrib.auth.mixins import AccessMixin

class SoloUsuariosPremiumMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.es_premium:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
```

### Decorador Personalizado
```python
from django.http import HttpResponseForbidden

def solo_usuarios_premium(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.es_premium:
            return HttpResponseForbidden("Acceso denegado")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
```

