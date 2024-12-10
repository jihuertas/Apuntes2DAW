Las validaciones en Django se realizan principalmente para asegurarse de que los datos que se ingresan en los formularios o se guardan en la base de datos sean correctos y coherentes. Django proporciona varios mecanismos para realizar estas validaciones, tanto a nivel de **modelos** como de **formularios**.

Veamos cómo funcionan las validaciones en Django en ambos niveles:

---

### **1. Validaciones a Nivel de Modelo**
Cuando defines un modelo en Django, puedes utilizar varios métodos y campos de validación para asegurarte de que los datos sean correctos antes de ser guardados en la base de datos.

#### **1.1. Validaciones en Campos del Modelo**

Django proporciona varios tipos de validadores que puedes usar en los campos del modelo, como `max_length`, `min_length`, `validators`, etc. Estos validadores son realizados automáticamente cuando guardas el objeto en la base de datos.

**Ejemplo de validación en el modelo:**

```python
from django.db import models
from django.core.exceptions import ValidationError

def validate_nombre(value):
    if value.lower() == "desconocido":
        raise ValidationError("El nombre no puede ser 'desconocido'.")

class Artista(models.Model):
    nombre = models.CharField(max_length=100, validators=[validate_nombre])
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
```

En este ejemplo, se define un validador personalizado `validate_nombre` que no permite que el nombre sea "desconocido". Este validador se ejecuta cuando el modelo intenta ser guardado en la base de datos.

---

#### **1.2. Método `clean` del Modelo**
El método `clean` en un modelo te permite realizar validaciones a nivel de toda la instancia del modelo (no solo de los campos individuales). Este método es útil si quieres validar condiciones entre varios campos.

**Ejemplo de validación con `clean`:**

```python
from django.core.exceptions import ValidationError
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        if self.nombre.lower() == 'desconocido':
            raise ValidationError("El nombre no puede ser 'desconocido'.")
        return super().clean()
```

El método `clean` permite realizar validaciones más complejas y personalizadas que involucren más de un campo.

---

#### **1.3. Validación al Guardar el Modelo**
Cuando intentas guardar un modelo, Django ejecuta las validaciones automáticamente:

```python
artista = Artista(nombre="Desconocido", fecha_nacimiento="2025-01-01")
artista.full_clean()  # Ejecuta las validaciones
artista.save()  # Si todo es válido, se guarda en la base de datos
```

Si alguna validación falla, Django lanzará un `ValidationError`, que puedes manejar para mostrar el error al usuario.

---

### **2. Validaciones a Nivel de Formulario**
Los formularios en Django permiten realizar validaciones tanto en los campos como a nivel del formulario completo. Los formularios proporcionan una capa adicional de validación antes de que los datos lleguen al modelo o la base de datos.

#### **2.1. Validación de un Solo Campo (Método `clean_<campo>`)**
Para realizar una validación específica en un campo de formulario, puedes sobrescribir el método `clean_<campo>`. Este método se llama automáticamente cuando el formulario es procesado.

**Ejemplo de validación de un solo campo:**

```python
from django import forms
from django.core.exceptions import ValidationError
from datetime import date

class ArtistaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        return fecha_nacimiento
```

- **`clean_<campo>`**: Este método valida el campo individual (en este caso, `fecha_nacimiento`). Si la fecha es mayor que la fecha actual, se lanza una excepción `ValidationError`.

---

#### **2.2. Validación a Nivel de Formulario (Método `clean`)**
El método `clean` en el formulario te permite realizar validaciones a nivel de varios campos al mismo tiempo. Aquí puedes validar reglas que dependan de la interacción entre los campos del formulario.

**Ejemplo de validación a nivel de formulario:**

```python
class ArtistaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        fecha_nacimiento = cleaned_data.get("fecha_nacimiento")

        if nombre.lower() == "desconocido" and fecha_nacimiento:
            raise ValidationError("El nombre 'desconocido' no puede tener una fecha de nacimiento.")
        
        return cleaned_data
```

- **`clean()`**: Este método se utiliza para validar condiciones entre varios campos. Si se cumplen ciertas condiciones, puedes lanzar un `ValidationError` que abarque todo el formulario.

---

#### **2.3. Validación de Formulario con `is_valid()`**
Cuando un formulario se envía, Django valida automáticamente los campos. Puedes comprobar si el formulario es válido con el método `is_valid()`:

```python
form = ArtistaForm(request.POST)
if form.is_valid():
    # Procesa los datos
    form.save()
else:
    # Muestra errores
    print(form.errors)
```

- **`is_valid()`**: Este método ejecuta todas las validaciones definidas en el formulario (incluyendo `clean_<campo>` y `clean()`) y retorna `True` si todos los campos son válidos.

---

### **3. Validadores Personalizados**
Django permite crear validadores personalizados que puedes usar en campos de modelos o formularios. Estos validadores pueden ser funciones o clases que validan un campo en específico.

**Ejemplo de un validador personalizado:**

```python
from django.core.exceptions import ValidationError

def validate_nombre(value):
    if value.lower() == "desconocido":
        raise ValidationError("El nombre no puede ser 'desconocido'.")
```

Este validador se puede aplicar a un campo del modelo o formulario, y se ejecutará cuando se valide el campo.

---

### **4. ¿Cómo Funciona el Flujo de Validación?**
1. **Modelos**:
   - **`clean`**: Se valida el modelo, verificando los valores de los campos y relaciones. Si se encuentra un error, se lanza un `ValidationError`.
   - **`full_clean()`**: Se llama para ejecutar la validación manualmente en el modelo.

2. **Formularios**:
   - **`clean_<campo>`**: Se valida cada campo individual.
   - **`clean()`**: Se valida el formulario completo, considerando las interacciones entre campos.
   - **`is_valid()`**: Ejecuta todas las validaciones y devuelve `True` si no se encuentran errores.

