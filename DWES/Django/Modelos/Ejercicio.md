# Actividad Propuesta

Crear una aplicación llamada **escuela** que incluya:

1. Un modelo `Profesor` (nombre, especialidad).
2. Un modelo `Asignatura` (nombre, profesor → ForeignKey).
3. Un modelo `Alumno` (nombre, edad).
4. Una relación ManyToMany entre `Alumno` y `Asignatura`.
5. (Opcional) Crear una tabla intermedia `Inscripcion` que incluya:

   * alumno
   * asignatura
   * fecha de inscripción
   * calificación

Deberás pensar qué relaciones son las adecuadas y justificar por qué se usa cada una.

---

# Solución del Ejercicio 

A continuación se muestra una propuesta de solución completa para la aplicación **escuela**, con los modelos definidos y las relaciones correctamente establecidas según lo pedido.

---

# 1. Modelo `Profesor`

Representa a un profesor con un nombre y una especialidad.

```python
from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"
```

---

# 2. Modelo `Asignatura`

Tiene un nombre y una relación **uno a muchos** con `Profesor`:
un profesor puede impartir varias asignaturas, pero cada asignatura solo tiene un profesor responsable.

```python
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="asignaturas")

    def __str__(self):
        return self.nombre
```

**Notas sobre la relación:**

* `ForeignKey` establece *uno a muchos*.
* `on_delete=models.CASCADE` asegura que si se elimina un profesor, se eliminan sus asignaturas.
* `related_name="asignaturas"` permite acceder desde un profesor a sus asignaturas así:

  ```python
  profesor.asignaturas.all()
  ```

---

# 3. Modelo `Alumno`

Representa a un alumno con nombre y edad.

```python
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
```

---

# 4. Relación Many-to-Many entre `Alumno` y `Asignatura`

Versión simple, sin tabla intermedia:

```python
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    asignaturas = models.ManyToManyField(Asignatura, related_name="alumnos")

    def __str__(self):
        return self.nombre
```

Con esta relación:

* Un alumno puede estar matriculado en muchas asignaturas.
* Una asignatura puede tener muchos alumnos.
* Django crea automáticamente una tabla intermedia.

---

# 5. Versión Opcional: Tabla Intermedia `Inscripcion`

Si se quiere añadir más información sobre la relación (fecha de inscripción, nota):

## 5.1 Modelo `Inscripcion`

```python
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha = models.DateField()
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('alumno', 'asignatura')

    def __str__(self):
        return f"{self.alumno} → {self.asignatura}"
```

**Notas:**

* Se usa `unique_together` para evitar duplicar matrículas del mismo alumno y asignatura.
* Campos como `fecha` o `calificacion` enriquecen la relación.
* El borrado en cascada elimina las inscripciones si desaparece el alumno o la asignatura.

---

## 5.2 Modificación del modelo `Alumno` para usar la tabla intermedia

```python
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    asignaturas = models.ManyToManyField(Asignatura, through='Inscripcion', related_name="alumnos")

    def __str__(self):
        return self.nombre
```

Ahora la relación Many-to-Many pasa por la tabla `Inscripcion`.

---

# Diagrama de la Solución (versión con tabla intermedia)

```
Profesor 1 ────────┐
                   │ (imparte)
Asignatura * <─────┘

Alumno * ──────────────* Asignatura
        (a través de Inscripcion)

Inscripcion:
    alumno_id  → FK Alumno
    asignatura_id → FK Asignatura
    fecha
    calificacion
```

