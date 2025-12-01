
# Relaciones Entre Modelos en Django

En proyectos reales, rara vez trabajarás con modelos aislados. Las relaciones permiten conectar modelos entre sí, tal como funcionan las tablas en bases de datos relacionales.

Django ofrece tres tipos principales de relaciones:

* **OneToOneField**
* **ForeignKey** (uno a muchos)
* **ManyToManyField**

A continuación se explican en profundidad.

---

## Relación One-to-One (Uno a Uno)

Una relación uno a uno significa que un registro de un modelo está relacionado con **exactamente un registro** de otro modelo, y al revés.

Es muy útil cuando quieres **extender** un modelo ya existente sin modificarlo, por ejemplo, ampliar el modelo `User` de Django con más información.

Ejemplo:

```python
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()
```

### Detalles importantes:

* Django crea una **restricción de unicidad**: un usuario no puede tener dos perfiles.
* La relación se guarda internamente como una clave única.
* Si se elimina el objeto relacionado (aquí `User`), el perfil también se elimina porque se usa `on_delete=models.CASCADE`.
* Permite acceder en ambos sentidos:

  * `perfil.usuario`
  * `usuario.perfil` (Django crea un atributo automáticamente, o puedes definirlo con `related_name`).

---

## Relación One-to-Many (Uno a Muchos) – ForeignKey

Se usa cuando un objeto pertenece a otro, pero el segundo puede tener muchos relacionados.

Ejemplo típico:
Un autor puede tener muchos libros, pero cada libro solo tiene un autor.

```python
class Autor(models.Model):
    nombre = models.CharField(max_length=50)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
```

### Detalles importantes:

* Esta relación se representa mediante una **clave foránea** en la tabla "muchos" (libros).
* `on_delete` determina qué sucede si el autor se elimina:

  * `CASCADE`: se eliminan también los libros.
  * `SET_NULL`: se mantiene el libro pero con el autor vacío → requiere `null=True`.
  * `PROTECT`: impide eliminar si tiene libros asociados.
  * `SET_DEFAULT`: sustituye por un valor por defecto.
* Se puede acceder en ambos sentidos:

  * Desde un libro: `libro.autor`
  * Desde un autor, Django genera: `autor.libro_set.all()`

    * Se puede cambiar el nombre con `related_name="libros"`.

---

## Relación Many-to-Many (Muchos a Muchos)

Se utiliza cuando **muchos** elementos del modelo A pueden estar relacionados con **muchos** elementos del modelo B.

Ejemplo: estudiantes y cursos.

```python
class Curso(models.Model):
    nombre = models.CharField(max_length=100)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso)
```

### ¿Qué sucede internamente?

Django crea automáticamente una **tabla intermedia** con dos columnas:

* `estudiante_id`
* `curso_id`

Cada fila representa una relación.

### Características de Many-to-Many:

* Una instancia puede tener múltiples objetos relacionados.
* Pueden modificarse las relaciones sin tocar los modelos.
* Accesos bidireccionales:

  * `estudiante.cursos.all()`
  * `curso.estudiante_set.all()`
* Es posible personalizar la tabla intermedia si necesitas guardar más información sobre la relación, por ejemplo, fecha de inscripción o nota obtenida:

```python
class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    nota = models.DecimalField(max_digits=4, decimal_places=2)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, through='Matricula')
```

Con esto se tiene un control total sobre la relación, convirtiéndola en un modelo explícito.





