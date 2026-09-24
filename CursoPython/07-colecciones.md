# 07. Listas, tuplas, conjuntos y diccionarios

## Objetivos

Aprender a almacenar y procesar varios valores relacionados mediante las principales colecciones incorporadas en Python.

## 1. ¿Por qué necesitamos colecciones?

Sin colecciones podríamos terminar con:

```python
alumno1 = "Ana"
alumno2 = "Luis"
alumno3 = "Marta"
```

Con una lista:

```python
alumnos = ["Ana", "Luis", "Marta"]
```

Ahora podemos recorrer, añadir, buscar y eliminar elementos de manera general.

# Listas

## 2. Crear una lista

```python
alumnos = ["Ana", "Luis", "Marta"]
```

Una lista:

- Mantiene el orden.
- Permite duplicados.
- Es mutable.
- Puede contener valores de distintos tipos.

## 3. Acceso por índice

```python
print(alumnos[0])
print(alumnos[1])
print(alumnos[-1])
```

## 4. Modificar

```python
alumnos[0] = "Antonio"
```

## 5. Añadir

```python
alumnos.append("Carlos")
```

Insertar en una posición:

```python
alumnos.insert(1, "Lucía")
```

## 6. Eliminar

Por valor:

```python
alumnos.remove("Luis")
```

Por posición:

```python
eliminado = alumnos.pop(0)
```

Último elemento:

```python
ultimo = alumnos.pop()
```

## 7. Longitud

```python
print(len(alumnos))
```

## 8. Pertenencia

```python
if "Ana" in alumnos:
    print("Ana está en la lista")
```

## 9. Recorrer listas

```python
for alumno in alumnos:
    print(alumno)
```

Con posición:

```python
for indice, alumno in enumerate(alumnos):
    print(indice, alumno)
```

Podemos comenzar a numerar en 1:

```python
for indice, alumno in enumerate(alumnos, start=1):
    print(indice, alumno)
```

## 10. Slicing

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])
print(numeros[:3])
print(numeros[2:])
print(numeros[::2])
```

## 11. Ordenar

Modificar la lista:

```python
alumnos.sort()
```

Obtener una nueva:

```python
ordenados = sorted(alumnos)
```

Descendente:

```python
alumnos.sort(reverse=True)
```

## 12. Funciones útiles

```python
notas = [7, 8, 5, 9]

print(len(notas))
print(min(notas))
print(max(notas))
print(sum(notas))
```

Media:

```python
media = sum(notas) / len(notas)
```

## 13. Comprensiones de listas

Forma tradicional:

```python
cuadrados = []

for numero in range(10):
    cuadrados.append(numero ** 2)
```

Comprensión:

```python
cuadrados = [numero ** 2 for numero in range(10)]
```

Con condición:

```python
pares = [numero for numero in range(20) if numero % 2 == 0]
```

Deben utilizarse cuando sigan siendo fáciles de leer.

# Tuplas

## 14. Crear una tupla

```python
coordenada = (10, 20)
```

Las tuplas son ordenadas e inmutables.

```python
coordenada[0] = 30
```

produciría un error.

## 15. Desempaquetado

```python
x, y = coordenada
```

Muy habitual cuando una función devuelve varios valores.

# Conjuntos

## 16. Crear un conjunto

```python
lenguajes = {"Python", "Java", "JavaScript"}
```

Los conjuntos:

- No mantienen elementos duplicados.
- Son útiles para pertenencia y operaciones de conjuntos.

```python
lenguajes = {"Python", "Java", "Python"}
print(lenguajes)
```

`Python` aparecerá una sola vez.

## 17. Añadir y eliminar

```python
lenguajes.add("C#")
lenguajes.remove("Java")
```

## 18. Operaciones

```python
grupo_a = {"Ana", "Luis", "Marta"}
grupo_b = {"Luis", "Marta", "Carlos"}
```

Unión:

```python
print(grupo_a | grupo_b)
```

Intersección:

```python
print(grupo_a & grupo_b)
```

Diferencia:

```python
print(grupo_a - grupo_b)
```

# Diccionarios

## 19. Crear un diccionario

```python
alumno = {
    "nombre": "Ana",
    "edad": 18,
    "nota": 8.5,
}
```

Los diccionarios almacenan pares **clave-valor**.

## 20. Acceder a valores

```python
print(alumno["nombre"])
```

Si la clave no existe se genera `KeyError`.

## 21. `get()`

```python
telefono = alumno.get("telefono")
```

No produce error si la clave no existe.

Valor por defecto:

```python
telefono = alumno.get("telefono", "No disponible")
```

## 22. Modificar y añadir

```python
alumno["nota"] = 9
alumno["email"] = "ana@example.com"
```

## 23. Eliminar

```python
alumno.pop("edad")
```

## 24. Recorrer un diccionario

Claves:

```python
for clave in alumno:
    print(clave)
```

Valores:

```python
for valor in alumno.values():
    print(valor)
```

Claves y valores:

```python
for clave, valor in alumno.items():
    print(clave, valor)
```

## 25. Estructuras anidadas

```python
alumnos = [
    {
        "nombre": "Ana",
        "notas": [7, 8, 9],
    },
    {
        "nombre": "Luis",
        "notas": [5, 6, 7],
    },
]
```

Acceso:

```python
print(alumnos[0]["nombre"])
print(alumnos[0]["notas"][1])
```

Recorrer:

```python
for alumno in alumnos:
    media = sum(alumno["notas"]) / len(alumno["notas"])
    print(f'{alumno["nombre"]}: {media:.2f}')
```

## 26. Elegir la colección adecuada

- **Lista**: colección ordenada que cambia.
- **Tupla**: secuencia ordenada que conceptualmente no debería cambiar.
- **Conjunto**: valores únicos y operaciones de pertenencia/conjuntos.
- **Diccionario**: información asociada a claves.

# Ejercicios con listas

En estos ejercicios practicaremos el uso de **listas en Python**, combinándolas con estructuras condicionales y bucles.

---

## Ejercicio 1. Análisis de temperaturas

Crea un programa que solicite al usuario las temperaturas registradas durante **7 días** y las almacene en una lista.

Una vez introducidas todas las temperaturas, el programa debe mostrar:

- La lista con todas las temperaturas.
- La temperatura máxima.
- La temperatura mínima.
- La temperatura media.
- Cuántos días tuvieron una temperatura superior a la media.
- Cuántos días tuvieron una temperatura inferior a 10 °C.

### Ampliación

Muestra también qué día de la semana tuvo la temperatura más alta.

Puedes utilizar la siguiente lista:

```python
dias = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
]
```

---

## Ejercicio 2. Lista de la compra

Crea un programa para gestionar una lista de la compra.

Comienza creando una lista vacía:

```python
compra = []
```

El programa debe solicitar productos al usuario y añadirlos a la lista.

La introducción de productos terminará cuando el usuario escriba:

```text
fin
```

Una vez terminada la introducción de productos:

1. Muestra la lista completa.
2. Muestra el número de productos introducidos.
3. Solicita al usuario el nombre de un producto que quiera eliminar.
4. Si el producto existe, elimínalo de la lista.
5. Si el producto no existe, muestra un mensaje indicándolo.
6. Muestra finalmente la lista resultante.

Ejemplo:

```text
Introduce un producto: Leche
Introduce un producto: Pan
Introduce un producto: Huevos
Introduce un producto: Arroz
Introduce un producto: fin

Lista de la compra:
['Leche', 'Pan', 'Huevos', 'Arroz']

Producto que quieres eliminar: Pan

Lista actualizada:
['Leche', 'Huevos', 'Arroz']
```

### Ampliación

Modifica el programa para impedir que pueda introducirse dos veces el mismo producto.

---

## Ejercicio 3. Aprobados y suspensos

Disponemos de la siguiente lista de notas:

```python
notas = [7.5, 4.2, 8.1, 3.7, 5.0, 9.3, 2.8, 6.4, 4.9, 7.2]
```

Crea dos listas vacías:

```python
aprobados = []
suspensos = []
```

Recorre la lista `notas` y almacena:

- En `aprobados` las notas iguales o superiores a `5`.
- En `suspensos` las notas inferiores a `5`.

Finalmente, el programa debe mostrar:

- La lista de notas original.
- La lista de aprobados.
- La lista de suspensos.
- El número de aprobados.
- El número de suspensos.
- El porcentaje de aprobados.
- La nota media de la clase.

Ejemplo de salida:

```text
Notas: [7.5, 4.2, 8.1, 3.7, 5.0, 9.3, 2.8, 6.4, 4.9, 7.2]

Aprobados: [7.5, 8.1, 5.0, 9.3, 6.4, 7.2]
Suspensos: [4.2, 3.7, 2.8, 4.9]

Número de aprobados: 6
Número de suspensos: 4
Porcentaje de aprobados: 60.0 %
Nota media: 5.91
```

### Restricción

Calcula la nota media recorriendo la lista.

**No puedes utilizar `sum()`.**

---

## Ejercicio 4. Eliminar elementos duplicados

Tenemos una lista con los identificadores de los alumnos que han accedido a una plataforma:

```python
accesos = [12, 7, 5, 12, 8, 7, 15, 5, 9, 12, 3, 8]
```

Un mismo alumno puede aparecer varias veces porque ha accedido a la plataforma en diferentes ocasiones.

Crea una nueva lista llamada:

```python
usuarios = []
```

Esta lista debe contener cada identificador **una sola vez**, manteniendo el orden de su primera aparición.

Para los datos anteriores, el resultado debería ser:

```python
[12, 7, 5, 8, 15, 9, 3]
```

El programa debe mostrar:

- La lista original de accesos.
- La lista de usuarios sin repetir.
- El número total de accesos.
- El número de usuarios diferentes.
- El número de accesos repetidos.

### Restricción

Debes resolver el ejercicio utilizando listas.

**No puedes utilizar `set()`.**

---

## Ejercicio 5. Clasificación de un torneo

Disponemos de dos listas:

```python
jugadores = ["Ana", "Luis", "Marta", "Pedro", "Lucía"]
puntos = [125, 80, 150, 95, 110]
```

Las posiciones de ambas listas están relacionadas.

Por ejemplo:

- `Ana` tiene `125` puntos.
- `Luis` tiene `80` puntos.
- `Marta` tiene `150` puntos.
- `Pedro` tiene `95` puntos.
- `Lucía` tiene `110` puntos.

El programa debe recorrer las listas y mostrar inicialmente:

```text
Ana - 125 puntos
Luis - 80 puntos
Marta - 150 puntos
Pedro - 95 puntos
Lucía - 110 puntos
```

A continuación debe determinar:

- El jugador con mayor puntuación.
- El jugador con menor puntuación.
- La puntuación media.
- Los jugadores que tienen una puntuación superior a la media.

Finalmente, muestra una clasificación ordenada de mayor a menor puntuación:

```text
CLASIFICACIÓN

1. Marta - 150 puntos
2. Ana - 125 puntos
3. Lucía - 110 puntos
4. Pedro - 95 puntos
5. Luis - 80 puntos
```

### Reto

Realiza la ordenación de los jugadores **sin utilizar `sort()` ni `sorted()`**.

Para resolverlo tendrás que pensar cómo intercambiar elementos de las listas manteniendo la relación entre cada jugador y su puntuación.

# Práctica Final: gestión de alumnado

Crear un programa con el menú:

```text
1. Añadir alumno
2. Eliminar alumno
3. Buscar alumno
4. Añadir nota
5. Mostrar alumnado
6. Calcular media
0. Salir
```

Representación propuesta:

```python
alumnos = [
    {
        "nombre": "Ana",
        "notas": [7, 8],
    }
]
```

Esta práctica se reutilizará en los siguientes temas.

---

[Anterior: 06. Bucles](06-bucles.md) · [Índice](README.md) · [Siguiente: 08. Funciones](08-funciones.md)
