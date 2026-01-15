## ¿Qué es Django Messages Framework?

Es un sistema de Django para **guardar mensajes temporales** (mensajes “flash”) como:

* “Guardado correctamente”
* “Error al enviar el formulario”
* “No tienes permisos”

y mostrarlos **en la misma página o en la siguiente**, normalmente después de un `redirect`.

Se guardan en **sesión o cookies** y se eliminan cuando ya se han mostrado.

---

## Pasos para usarlo

## 1) Activarlo (casi siempre ya viene configurado)

En `settings.py` debe existir:

* `django.contrib.messages` en `INSTALLED_APPS`
* En `MIDDLEWARE`:

  * `django.contrib.sessions.middleware.SessionMiddleware`
  * `django.contrib.messages.middleware.MessageMiddleware`
* En `TEMPLATES` → context processors:

  * `django.contrib.messages.context_processors.messages`

Esto permite que la variable `messages` esté disponible en los templates.

---

## 2) Crear mensajes desde la vista

```python
from django.contrib import messages

messages.success(request, "Guardado correctamente")
messages.error(request, "Ha ocurrido un error")
messages.warning(request, "Revisa los datos")
messages.info(request, "Información extra")
```

Esto guarda un mensaje asociado a esa petición, con un nivel (success, error, etc.).

---

## 3) Mostrar mensajes en el template

```django
{% if messages %}
  {% for message in messages %}
    <div class="{{ message.tags }}">
      {{ message }}
    </div>
  {% endfor %}
{% endif %}
```

* `messages` contiene los mensajes pendientes
* `message.tags` te da una clase útil para CSS (`success`, `error`, etc.)
* Cuando se muestran, normalmente ya no vuelven a aparecer

---

## 4) Uso típico con redirect

```python
from django.shortcuts import redirect
from django.contrib import messages

messages.success(request, "Perfil actualizado")
return redirect("perfil")
```

Funciona porque Django guarda el mensaje y lo enseña en la siguiente página tras el redirect.
