# Bloque 7. Integridad de datos y transacciones

**UT4 · Persistencia: bases de datos y ORM**  
**Duración:** 2 horas  
**Requisitos:** proyecto `biblioteca` con modelos relacionados del bloque 6.

## Objetivos

- Identificar restricciones que protegen la integridad de los datos.
- Diferenciar validación de Django y restricciones de la base de datos.
- Ejecutar operaciones relacionadas de forma atómica.
- Comprobar que una transacción se revierte cuando ocurre un error.

## 1. ¿Qué es la integridad de los datos?

La integridad garantiza que la información almacenada respete las reglas del sistema. Ejemplos: un ISBN no debe repetirse, un préstamo debe referirse a un libro existente y no debe registrarse dos veces un préstamo activo del mismo libro.

| Mecanismo | Ejemplo | Efecto |
|---|---|---|
| `unique=True` | ISBN | Impide duplicados en la base de datos |
| `null=False` | Título obligatorio en almacenamiento | Impide `NULL` |
| `ForeignKey` | Préstamo → Libro | Mantiene la referencia entre tablas |
| `CheckConstraint` | Precio no negativo | Restringe valores admitidos |
| `on_delete=PROTECT` | Editorial con libros | Impide su eliminación desde el ORM |

## 2. Restricciones en modelos

Podemos definir una restricción sobre el precio de `Libro`. Añádela dentro de la clase `Meta` existente del modelo (conservando otras opciones que ya tenga):

```python
from django.db import models
from django.db.models import Q

class Meta:
    ordering = ["titulo"]
    constraints = [
        models.CheckConstraint(
            condition=Q(precio__gte=0),
            name="libro_precio_no_negativo",
        ),
    ]
```

Tras modificar el modelo:

```bash
python manage.py makemigrations catalogo
python manage.py migrate
```

**Importante:** `blank=False` es una regla de validación de Django; `save()` no ejecuta automáticamente `full_clean()`. Las restricciones de base de datos son una protección adicional, no sustituyen todas las validaciones de aplicación.

## 3. ¿Qué es una transacción?

Una transacción agrupa varias operaciones de base de datos como una unidad: **o se confirman todas o se deshacen todas**. Es fundamental cuando una acción requiere cambiar más de un registro.

Ejemplo: registrar un préstamo y marcar un libro como no disponible. Si falla la creación del préstamo, el libro no debe quedar marcado como prestado.

## 4. Modelo Prestamo

Añade a `catalogo/models.py` (conservando los demás modelos):

```python
from django.conf import settings
from django.db import models

class Prestamo(models.Model):
    libro = models.ForeignKey(
        "Libro", on_delete=models.PROTECT,
        related_name="prestamos"
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="prestamos_biblioteca"
    )
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Préstamo {self.pk}: {self.libro}"
```

Aplica las migraciones:

```bash
python manage.py makemigrations catalogo
python manage.py migrate
```

## 5. Registrar un préstamo con transaction.atomic()

El siguiente ejemplo se ejecuta dentro del contexto de Django (shell o módulo importado por Django). `select_for_update()` bloquea la fila durante la transacción en gestores compatibles, como PostgreSQL; **SQLite no aplica ese bloqueo de filas**, por lo que el ejemplo no debe considerarse suficiente para gestionar concurrencia real en SQLite.

```python
from django.db import transaction
from catalogo.models import Libro, Prestamo


def prestar_libro(libro_id, usuario):
    with transaction.atomic():
        libro = Libro.objects.select_for_update().get(pk=libro_id)
        if not libro.disponible:
            raise ValueError("El libro no está disponible")

        prestamo = Prestamo.objects.create(
            libro=libro,
            usuario=usuario,
        )
        libro.disponible = False
        libro.save(update_fields=["disponible"])
        return prestamo
```

El uso de `atomic()` asegura que, si una excepción sale del bloque, las operaciones de la transacción se revierten. En una aplicación con usuarios concurrentes será necesario diseñar además restricciones y mecanismos de bloqueo adecuados al gestor utilizado.

## 6. Devolver un libro

```python
from django.utils import timezone


def devolver_libro(prestamo_id):
    with transaction.atomic():
        prestamo = Prestamo.objects.select_for_update().get(pk=prestamo_id)
        if prestamo.fecha_devolucion is not None:
            raise ValueError("El préstamo ya fue devuelto")

        prestamo.fecha_devolucion = timezone.now()
        prestamo.save(update_fields=["fecha_devolucion"])
        prestamo.libro.disponible = True
        prestamo.libro.save(update_fields=["disponible"])
```

Este ejemplo didáctico supone que cada libro solo puede tener un préstamo activo y que `disponible` refleja ese estado. Una implementación completa debería reforzar esta regla con restricciones y pruebas.

## 7. Comprobar una reversión (rollback)

Para observar el efecto de una transacción, fuerza un error **después** de modificar un libro:

```python
from django.db import transaction
from catalogo.models import Libro

libro = Libro.objects.filter(disponible=True).first()
if libro is not None:
    try:
        with transaction.atomic():
            libro.disponible = False
            libro.save(update_fields=["disponible"])
            raise RuntimeError("Error simulado")
    except RuntimeError:
        pass

    libro.refresh_from_db()
    print(libro.disponible)  # True: el cambio se ha revertido
```

El error se captura **fuera** de `atomic()` para que la transacción detecte la excepción y se revierta.

## Demostración guiada (35 min)

1. Revisar las restricciones ya existentes (`unique`, relaciones y `on_delete`).
2. Añadir la restricción de precio y migrarla.
3. Crear el modelo `Prestamo` y migrarlo.
4. Ejecutar una operación de préstamo válida.
5. Simular un error y comprobar el rollback con `refresh_from_db()`.

## Actividad 7. Préstamos e integridad (65 min)

**Enunciado:** Amplía la biblioteca para gestionar préstamos con operaciones consistentes.

1. Añade el modelo `Prestamo` y aplica las migraciones.
2. Incorpora una restricción que impida precios negativos en `Libro`.
3. Implementa `prestar_libro(libro_id, usuario)` con `transaction.atomic()`.
4. Impide prestar un libro marcado como no disponible.
5. Implementa `devolver_libro(prestamo_id)` para registrar la fecha de devolución y volver a marcar el libro como disponible.
6. Impide devolver dos veces el mismo préstamo.
7. Simula un error dentro de una transacción y comprueba que el cambio se revierte.
8. Explica por qué `select_for_update()` no proporciona bloqueo de filas en SQLite y qué cambia al utilizar PostgreSQL.

**Entrega:** modelos y migraciones, archivo con las funciones de préstamo/devolución, y pruebas de un préstamo correcto, una operación rechazada y un rollback.

**Preguntas:** ¿Por qué no basta con cambiar `disponible` sin crear el préstamo? ¿Qué diferencia existe entre validación de Django y restricción de base de datos? ¿Qué ocurre si una excepción sale del bloque `atomic()`?

## Distribución de las 2 horas

| Fase | Tiempo |
|---|---:|
| Explicación de integridad y transacciones | 20 min |
| Demostración guiada | 35 min |
| Actividad autónoma y revisión | 65 min |

## Comprobación de aprendizaje

- [ ] Reconozco las principales restricciones de integridad.
- [ ] Creo y aplico migraciones de restricciones y modelos.
- [ ] Agrupo cambios relacionados con `transaction.atomic()`.
- [ ] Compruebo el rollback ante un error.
- [ ] Distingo el comportamiento de SQLite y PostgreSQL en operaciones concurrentes.

**Siguiente bloque:** panel de administración de Django.
