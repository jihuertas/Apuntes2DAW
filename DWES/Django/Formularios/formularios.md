Veamos cómo funcionan los formularios en HTML y cómo puedes crearlos en Django utilizando tanto formularios simples con `forms.Form` como formularios basados en modelos con `forms.ModelForm`. También veremos cómo integrarlos con vistas basadas en funciones (function-based views, FBV) y cómo trabajar con las plantillas.

---

### **1. Formularios en HTML**

En HTML, los formularios son una manera de recolectar datos del usuario a través de campos como texto, fechas, números, etc. Los formularios se envían típicamente usando el método `POST` para que los datos sean procesados por el servidor.

#### **1.1. Estructura Básica de un Formulario en HTML**

Aquí tienes un ejemplo simple de un formulario en HTML:

```html
<form method="POST" action="/guardar_datos/">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre">
    
    <label for="fecha_nacimiento">Fecha de Nacimiento:</label>
    <input type="date" id="fecha_nacimiento" name="fecha_nacimiento">
    
    <button type="submit">Enviar</button>
</form>
```

- **`method="POST"`**: Indica que el formulario enviará los datos usando el método POST.
- **`action="/guardar_datos/"`**: La URL a la que se enviarán los datos para ser procesados.
- **`<label>` y `<input>`**: Definen los campos que el usuario completará (en este caso, un campo de texto y uno de fecha).

---

### **2. Formularios en Django con `forms.Form`**

En Django, puedes crear formularios de distintas maneras. Aquí te mostramos dos: con **formularios basados en clases** (`forms.Form`) o **formularios basados en modelos** (`forms.ModelForm`). Empezaremos viendo cómo crear un formulario con `forms.Form`, cómo integrarlo con una vista basada en función (FBV) y cómo usar una plantilla para mostrar el formulario.

#### **2.1. Crear un Formulario con `forms.Form`**

Django proporciona la clase `forms.Form` para definir formularios manualmente. Estos formularios de debern crear dentro de un archivo `forms.py` (que hay que crear en la app). Vemos un ejemplo de un formulario para que el usuario ingrese datos sobre un artista.

```python
from django import forms

class ArtistaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Artista')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label='Correo Electrónico')
```

- **`CharField`**: Campo de texto para el nombre del artista.
- **`DateField`**: Campo de fecha para la fecha de nacimiento. Usamos el widget `DateInput` para hacer que el navegador muestre un selector de fecha.
- **`EmailField`**: Campo para el correo electrónico.

#### **2.2. Crear una Vista para Manejar el Formulario**

En Django, puedes crear vistas basadas en funciones (FBV) para procesar formularios. Aquí, creamos una vista que maneja la visualización y el procesamiento de nuestro formulario.

```python
from django.shortcuts import render, redirect
from .forms import ArtistaForm

def agregar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        
        # Validar el formulario
        if form.is_valid():
            # Aquí procesas los datos, por ejemplo, creando un modelo con esos datos
            nombre = form.cleaned_data['nombre']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            email = form.cleaned_data['email']
            
            # Redirigir a otra página (por ejemplo, a la lista de artistas)
            return redirect('artistas_lista')  # Cambia 'artistas_lista' por la URL de destino

    else:
        form = ArtistaForm()  # Si el método no es POST, crear el formulario vacío

    return render(request, 'agregar_artista.html', {'form': form})
```

- **`request.method == 'POST'`**: Verificamos si el formulario fue enviado.
- **`form.is_valid()`**: Validamos los datos enviados. Si el formulario es válido, se pueden procesar.
- **`form.cleaned_data`**: Este diccionario contiene los datos limpios (validados) del formulario.
- **`redirect`**: Después de procesar los datos, redirigimos a otra página, como la lista de artistas.

#### **2.3. Plantilla para Mostrar el Formulario**

En la plantilla HTML, renderizamos el formulario y mostramos los errores si los datos no son válidos. A continuación, un ejemplo de la plantilla `agregar_artista.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Agregar Artista</title>
</head>
<body>
    <h1>Agregar Artista</h1>
    
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar Artista</button>
    </form>
    
    {% if form.errors %}
        <ul>
            {% for field in form %}
                {% for error in field.errors %}
                    <li>{{ error }}</li>
                {% endfor %}
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
```

- **`{% csrf_token %}`**: Django genera un token CSRF para proteger contra ataques de falsificación de solicitudes entre sitios.
- **`{{ form.as_p }}`**: Muestra el formulario en un formato de párrafos.
- **`form.errors`**: Muestra los errores de validación si los hay.

#### **2.4. URL para Acceder a la Vista**

Finalmente, debes definir la URL en el archivo `urls.py` para acceder a la vista `agregar_artista`.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('agregar_artista/', views.agregar_artista, name='agregar_artista'),
]
```

---

### **3. Formularios en Django con `forms.ModelForm`**

Si deseas trabajar con formularios que estén directamente relacionados con los modelos de Django (por ejemplo, para crear o actualizar registros en la base de datos), puedes usar `forms.ModelForm`. Esto permite crear formularios que se basan en un modelo específico y que gestionan automáticamente la validación y la conversión de los datos a un formato adecuado para guardar en la base de datos.

#### **3.1. Crear un `ModelForm`**

Primero, definimos un modelo para el artista en `models.py`:

```python
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre
```

Luego, creamos un `ModelForm` para este modelo:

```python
from django import forms
from .models import Artista

class ArtistaModelForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'fecha_nacimiento', 'email']
```

- **`ModelForm`**: Es una clase que automáticamente genera un formulario basado en el modelo. No necesitamos definir cada campo, ya que se infiere del modelo.
- **`fields`**: Especifica qué campos del modelo se incluirán en el formulario.

#### **3.2. Vista para Manejar un `ModelForm`**

El proceso en la vista es similar al de un formulario normal, pero ahora usaremos `ArtistaModelForm` en lugar de `ArtistaForm`. Django maneja automáticamente la creación o actualización de los registros en la base de datos.

```python
from django.shortcuts import render, redirect
from .forms import ArtistaModelForm

def agregar_artista(request):
    if request.method == 'POST':
        form = ArtistaModelForm(request.POST)
        
        if form.is_valid():
            # Guardamos los datos en el modelo (esto crea un nuevo Artista en la base de datos)
            form.save()
            return redirect('artistas_lista')

    else:
        form = ArtistaModelForm()

    return render(request, 'agregar_artista.html', {'form': form})
```

- **`form.save()`**: Django guarda automáticamente los datos del formulario en la base de datos. Si el formulario es nuevo, crea una nueva entrada; si está editando un registro, lo actualiza.

Si lo que queremos es editar un artista, realizaremos algo muy parecido:

```python
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtistaModelForm
from .models import Artista

def editar_artista(request, pk):
    
    if request.method == 'POST':
        form = ArtistaModelForm(request.POST)
        
        if form.is_valid():
            # Guardamos los datos en el modelo (esto edita los datos del Artista en la base de datos)
            form.save()
            return redirect('artistas_lista')

    else:
        artista = get_object_or_404(Artista, pk=pk)
        form = ArtistaModelForm(instance=artista)

    return render(request, 'editar_artista.html', {'form': form})
```

#### **3.3. Plantilla y URL**

La plantilla y la URL son las mismas que en el ejemplo con `forms.Form`. No es necesario hacer cambios en el HTML ni en el archivo `urls.py`.

