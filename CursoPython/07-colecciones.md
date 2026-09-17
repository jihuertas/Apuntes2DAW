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

## 27. Práctica: gestión de alumnado

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
