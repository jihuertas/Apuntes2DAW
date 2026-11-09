# Bloque 5. Consultas ORM: filtrado, ordenación y agregación


## Objetivos

- Recuperar registros con `all()`, `get()`, `filter()` y `exclude()`.
- Construir consultas con operadores de búsqueda (*lookups*).
- Ordenar, limitar y combinar consultas.
- Calcular estadísticas con `aggregate()` y `annotate()`.

## 1. QuerySets y consultas

Un `QuerySet` representa una consulta sobre registros de un modelo. Muchas operaciones son **perezosas**: Django no ejecuta la consulta hasta que necesita sus resultados (por ejemplo, al recorrerla o convertirla en lista).

```python
from catalogo.models import Libro

consulta = Libro.objects.filter(disponible=True)
for libro in consulta:
    print(libro.titulo)
```

`all()` devuelve todos los registros; `get()` devuelve exactamente uno o lanza una excepción; `filter()` devuelve un `QuerySet`, aunque esté vacío; `exclude()` excluye coincidencias.

```python
Libro.objects.all()
Libro.objects.filter(disponible=True)
Libro.objects.exclude(disponible=True)
Libro.objects.get(isbn="9780000000001")
```

## 2. Operadores de búsqueda

Django utiliza `campo__operador` (dos guiones bajos):

| Operador | Significado | Ejemplo |
|---|---|---|
| `exact` | Igualdad | `titulo__exact="Django práctico"` |
| `icontains` | Contiene texto, sin distinguir mayúsculas | `titulo__icontains="python"` |
| `startswith` | Comienza por | `titulo__startswith="El"` |
| `gt`, `gte` | Mayor que / mayor o igual | `precio__gte=20` |
| `lt`, `lte` | Menor que / menor o igual | `paginas__lt=300` |
| `in` | Pertenece a un conjunto | `pk__in=[1, 2, 3]` |
| `isnull` | Es nulo / no es nulo | `sinopsis__isnull=True` |
| `year` | Componente año de una fecha | `fecha_publicacion__year=2024` |

```python
Libro.objects.filter(titulo__icontains="django")
Libro.objects.filter(precio__gte=20, disponible=True)
Libro.objects.filter(fecha_publicacion__year__gte=2023)
```

## 3. Encadenar, ordenar y limitar

```python
# Libros disponibles con precio inferior a 30, por precio ascendente
Libro.objects.filter(disponible=True, precio__lt=30).order_by("precio")

# Orden descendente
Libro.objects.order_by("-precio")

# Los cinco primeros según un orden explícito
Libro.objects.order_by("titulo")[:5]

# Solo ciertos campos
Libro.objects.values("titulo", "precio")
```

`order_by("-campo")` ordena de forma descendente. El corte `[:5]` limita los resultados.

## 4. Condiciones OR con Q

```python
from django.db.models import Q

Libro.objects.filter(
    Q(titulo__icontains="python") | Q(titulo__icontains="django")
)

Libro.objects.filter(
    Q(precio__lt=15) & Q(disponible=True)
)
```

`|` representa OR y `&` representa AND. Los argumentos normales de `filter()` también se combinan con AND.

## 5. Agregaciones

Las agregaciones permiten obtener estadísticas de un conjunto de registros.

```python
from django.db.models import Avg, Count, Max, Min, Sum

Libro.objects.count()
Libro.objects.aggregate(precio_medio=Avg("precio"))
Libro.objects.aggregate(precio_maximo=Max("precio"))
Libro.objects.aggregate(precio_minimo=Min("precio"))
Libro.objects.aggregate(suma_precios=Sum("precio"))
```

`aggregate()` devuelve un diccionario con resultados globales. `annotate()` añade valores calculados a los elementos de una consulta. Sin relaciones todavía, podemos agrupar por disponibilidad:

```python
Libro.objects.values("disponible").annotate(
    total=Count("id"),
    precio_medio=Avg("precio"),
).order_by("disponible")
```

## 6. Ver el SQL generado

```python
consulta = Libro.objects.filter(precio__gte=20).order_by("titulo")
print(consulta.query)
```

La salida permite relacionar el código ORM con la consulta SQL. No es necesario escribir SQL manualmente para resolver las actividades.

## Demostración guiada 

1. Mostrar la diferencia entre `get()` y `filter()`.
2. Buscar títulos por fragmentos y precios por rangos.
3. Encadenar filtros y ordenar ascendente/descendente.
4. Combinar dos condiciones con `Q`.
5. Calcular número de libros, precio medio y precio máximo.
6. Agrupar por disponibilidad con `values().annotate()`.

## Actividad 5. Boletín de consultas ORM 

**Preparación:** utiliza al menos diez libros con títulos, fechas, precios y disponibilidades variadas. Si tu catálogo tiene menos registros, añade los necesarios mediante el ORM.

Resuelve las siguientes consultas **sin SQL directo**:

1. Mostrar todos los libros.
2. Obtener los libros disponibles.
3. Obtener los libros no disponibles.
4. Buscar libros cuyo título contenga `python`, sin distinguir mayúsculas.
5. Obtener libros con precio superior a 20 euros.
6. Obtener libros con precio entre 10 y 30 euros, ambos incluidos.
7. Obtener libros publicados a partir de 2023.
8. Mostrar libros ordenados alfabéticamente por título.
9. Mostrar libros ordenados por precio descendente.
10. Recuperar los tres libros más baratos.
11. Obtener libros disponibles con más de 250 páginas.
12. Buscar libros cuyo título contenga `python` **o** `django`.
13. Calcular el número total de libros.
14. Calcular el precio medio, máximo y mínimo.
15. Agrupar por disponibilidad e indicar el número de libros de cada grupo.

**Entrega:** archivo `actividad5_consultas.py` con las consultas comentadas y sus resultados, ejecutable mediante `python manage.py shell < actividad5_consultas.py`. No es necesario crear vistas ni plantillas.

**Preguntas:** ¿Por qué `filter()` no falla cuando no encuentra registros? ¿Qué diferencia existe entre `aggregate()` y `annotate()`? ¿Qué devuelve `values()`?



**Siguiente bloque:** relaciones uno a uno, uno a muchos y muchos a muchos.
