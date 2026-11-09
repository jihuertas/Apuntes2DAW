# Bloque 4. Operaciones CRUD y recuperación y modificación de información


## Objetivos

- Crear, recuperar, modificar y eliminar registros usando el ORM de Django.
- Diferenciar operaciones sobre instancias y operaciones sobre conjuntos de registros.
- Interpretar los errores habituales al recuperar objetos.
- Comprobar la persistencia de los cambios en SQLite.

## 1. ¿Qué significa CRUD?

CRUD corresponde a **Create, Read, Update, Delete**. Son las operaciones básicas de persistencia. Django las implementa a través del administrador `objects` de cada modelo y de sus `QuerySet`.

| Operación | Django ORM | Resultado |
|---|---|---|
| Crear | `objects.create()` | Inserta y devuelve una instancia |
| Leer | `objects.all()`, `objects.get()` | Obtiene registros |
| Modificar | `obj.save()`, `objects.filter(...).update()` | Guarda cambios |
| Eliminar | `obj.delete()`, `objects.filter(...).delete()` | Elimina registros |

## 2. Preparación del entorno

Desde la carpeta que contiene `manage.py`:

```bash
python manage.py shell
```

Los ejemplos usan el modelo `Libro` del bloque 2 con los campos `titulo`, `isbn`, `sinopsis`, `fecha_publicacion`, `paginas`, `precio`, `disponible` y, tras el bloque 3, `recomendado` e `idioma` si se añadieron. No se utilizan aún relaciones entre modelos.

```python
from datetime import date
from decimal import Decimal
from catalogo.models import Libro
```

## 3. Crear registros (Create)

```python
libro = Libro.objects.create(
    titulo="Python para todos",
    isbn="9780000000001",
    sinopsis="Introducción a Python",
    fecha_publicacion=date(2024, 5, 10),
    paginas=280,
    precio=Decimal("24.90"),
    disponible=True,
)
print(libro.pk, libro.titulo)
```

También se puede crear una instancia y guardarla después:

```python
otro = Libro(
    titulo="Django práctico",
    isbn="9780000000002",
    fecha_publicacion=date(2025, 2, 1),
    paginas=320,
    precio=Decimal("29.50"),
)
otro.save()
```

**Observación:** construir `Libro(...)` no lo almacena hasta llamar a `save()`. `objects.create(...)` sí lo almacena inmediatamente.

## 4. Recuperar información (Read)

```python
Libro.objects.all()
Libro.objects.count()
Libro.objects.first()
Libro.objects.get(pk=libro.pk)
```

`get()` espera exactamente un resultado: si no existe lanza `Libro.DoesNotExist`; si hay varios, `Libro.MultipleObjectsReturned`. Para búsquedas que pueden devolver varios registros utilizaremos `filter()` en el bloque 5.

```python
try:
    encontrado = Libro.objects.get(isbn="9780000000001")
    print(encontrado.titulo)
except Libro.DoesNotExist:
    print("No se ha encontrado el libro")
```

## 5. Modificar información (Update)

```python
libro = Libro.objects.get(isbn="9780000000001")
libro.precio = Decimal("21.95")
libro.disponible = False
libro.save()
```

Actualización directa sobre registros seleccionados:

```python
Libro.objects.filter(isbn="9780000000002").update(disponible=False)
```

`update()` devuelve el número de filas afectadas y **no llama al método `save()` de cada instancia**. Por eso no es equivalente en todos los casos a modificar objetos y guardarlos.

## 6. Eliminar información (Delete)

```python
libro = Libro.objects.get(isbn="9780000000002")
libro.delete()
```

También puede eliminarse un conjunto de registros:

```python
Libro.objects.filter(disponible=False).delete()
```

**Precaución:** `Libro.objects.all().delete()` elimina todos los registros del modelo. Antes de eliminar, inspecciona qué registros coinciden con el filtro.

## 7. Comprobar la persistencia

Sal del shell con `exit()`, vuelve a abrirlo y consulta los registros. Si siguen ahí, la información se ha persistido en la base de datos. También puedes abrir `db.sqlite3` con DB Browser for SQLite, preferiblemente con el shell cerrado.

## Demostración guiada (45 min)

1. Abrir Django Shell e importar `Libro`, `date` y `Decimal`.
2. Crear dos libros con ISBN diferentes.
3. Consultar sus identificadores y contar los registros.
4. Recuperar uno por ISBN y modificar su precio.
5. Marcar otro como no disponible con `update()`.
6. Eliminar solo uno y comprobar el resultado.
7. Cerrar y reabrir el shell para comprobar que los cambios permanecen.

## Actividad 4. Gestión CRUD del catálogo (90 min)

**Enunciado:** A partir del proyecto `biblioteca`, realiza las siguientes operaciones exclusivamente con el ORM desde Django Shell.

1. Crea **cinco libros** con ISBN distintos, título, fecha de publicación, páginas y precio.
2. Recupera todos los libros y muestra su título y precio mediante un bucle.
3. Recupera un libro por su ISBN y muestra todos sus campos.
4. Cambia el precio y la disponibilidad de dos libros usando instancias y `save()`.
5. Actualiza la disponibilidad de otro libro con `filter(...).update(...)`.
6. Intenta recuperar un ISBN inexistente y controla `DoesNotExist`.
7. Elimina un libro identificado por su ISBN, sin borrar los demás.
8. Cierra el shell, ábrelo de nuevo y comprueba los registros restantes.

**Entrega:** archivo `actividad4_crud.py` con las instrucciones ejecutadas (o transcripción ordenada del shell) y capturas de la consulta final. Si se utiliza un script, ejecútalo dentro del contexto de Django, por ejemplo con `python manage.py shell < actividad4_crud.py`.

**Preguntas:** ¿Qué diferencia hay entre `create()` y `save()`? ¿Qué ocurre al usar `get()` con un ISBN inexistente? ¿Qué riesgo tiene ejecutar `all().delete()`?

## Distribución de las 3 horas

| Fase | Tiempo |
|---|---:|
| Conceptos y explicación | 45 min |
| Demostración guiada | 45 min |
| Actividad autónoma y revisión | 90 min |

## Comprobación de aprendizaje

- [ ] Inserto registros con valores de tipos correctos.
- [ ] Recupero un registro concreto y gestiono su ausencia.
- [ ] Modifico información con `save()` y `update()`.
- [ ] Elimino únicamente los registros previstos.
- [ ] Compruebo que los cambios permanecen tras reiniciar el shell.

**Siguiente bloque:** consultas ORM, filtrado, ordenación y agregaciones.
