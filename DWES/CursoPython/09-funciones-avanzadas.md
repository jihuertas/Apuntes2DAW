# 09. `*args`, `**kwargs`, lambda y decoradores

## Objetivos

Profundizar en el funcionamiento de las funciones y comprender construcciones que aparecen con frecuencia en bibliotecas y frameworks de Python.

# `*args`

## 1. Número variable de argumentos posicionales

```python
def sumar(*numeros):
    return sum(numeros)
```

Podemos llamar:

```python
print(sumar(1, 2))
print(sumar(1, 2, 3))
print(sumar(1, 2, 3, 4, 5))
```

Dentro de la función, `numeros` es una tupla.

```python
def mostrar(*args):
    print(type(args))
    print(args)
```

## 2. Combinar parámetros normales y `*args`

```python
def registrar_notas(nombre, *notas):
    print(nombre)
    print(notas)
```

```python
registrar_notas("Ana", 7, 8, 9)
```

# `**kwargs`

## 3. Argumentos nombrados variables

```python
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
```

Uso:

```python
mostrar_datos(
    nombre="Ana",
    edad=18,
    curso="2º DAW",
)
```

Dentro de la función, `datos` es un diccionario.

## 4. Combinación completa

```python
def ejemplo(obligatorio, *args, **kwargs):
    print(obligatorio)
    print(args)
    print(kwargs)
```

Estas construcciones son frecuentes en frameworks porque permiten reenviar argumentos sin conocerlos todos de antemano.

# Desempaquetado

## 5. Desempaquetar una lista o tupla

```python
def sumar(a, b, c):
    return a + b + c

numeros = [10, 20, 30]
print(sumar(*numeros))
```

Es equivalente a:

```python
sumar(10, 20, 30)
```

## 6. Desempaquetar un diccionario

```python
def crear_usuario(nombre, edad):
    return {"nombre": nombre, "edad": edad}


datos = {
    "nombre": "Ana",
    "edad": 18,
}

usuario = crear_usuario(**datos)
```

Las claves deben coincidir con los nombres de los parámetros.

# Funciones lambda

## 7. Concepto

Una lambda permite crear una función pequeña mediante una expresión.

```python
doble = lambda numero: numero * 2
print(doble(5))
```

Equivale a:

```python
def doble(numero):
    return numero * 2
```

No debemos utilizar lambda para reemplazar cualquier función. Es útil cuando necesitamos una función sencilla y breve en un punto concreto.

## 8. Lambda como clave de ordenación

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 6},
    {"nombre": "Marta", "nota": 9},
]

alumnos.sort(key=lambda alumno: alumno["nota"])
```

Descendente:

```python
alumnos.sort(key=lambda alumno: alumno["nota"], reverse=True)
```

# Las funciones son objetos

## 9. Guardar una función en una variable

```python
def saludar():
    print("Hola")

funcion = saludar
funcion()
```

Es importante observar que:

```python
saludar
```

es la función, mientras que:

```python
saludar()
```

la ejecuta.

## 10. Funciones como argumentos

```python
def ejecutar(funcion):
    funcion()


def saludar():
    print("Hola")


ejecutar(saludar)
```

## 11. Funciones dentro de funciones

```python
def exterior():
    def interior():
        print("Función interior")

    interior()
```

Una función también puede devolver otra función.

# Decoradores

## 12. Idea general

Un decorador recibe una función y devuelve otra función que añade o modifica comportamiento.

```python
def registrar(funcion):
    def wrapper():
        print("Antes")
        funcion()
        print("Después")

    return wrapper
```

Podemos hacer manualmente:

```python
def saludar():
    print("Hola")

saludar = registrar(saludar)
saludar()
```

## 13. Sintaxis `@`

Python ofrece una sintaxis más cómoda:

```python
@registrar
def saludar():
    print("Hola")
```

Ahora:

```python
saludar()
```

produce:

```text
Antes
Hola
Después
```

## 14. Decoradores compatibles con argumentos

```python
def registrar(funcion):
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print("Ejecución finalizada")
        return resultado

    return wrapper
```

Uso:

```python
@registrar
def sumar(a, b):
    return a + b

print(sumar(4, 5))
```

## 15. `functools.wraps`

Un decorador sencillo puede ocultar metadatos de la función original. La solución habitual es `wraps`.

```python
from functools import wraps


def registrar(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {funcion.__name__}")
        return funcion(*args, **kwargs)

    return wrapper
```

## 16. Decorador para medir tiempo

```python
from functools import wraps
from time import perf_counter


def medir_tiempo(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = perf_counter()
        print(f"Tiempo: {fin - inicio:.6f} s")
        return resultado

    return wrapper
```

## 17. Relación con frameworks

Los decoradores aparecen con frecuencia en aplicaciones reales. Algunos frameworks los utilizan para:

- Controlar permisos.
- Registrar rutas.
- Validar acceso.
- Añadir caché.
- Gestionar transacciones.

Por eso es importante comprender la idea aunque no necesitemos construir decoradores complejos desde cero.

## 18. Actividades

### Actividad 1

Crea una función `media(*notas)` que acepte cualquier cantidad de notas.

### Actividad 2

Crea `crear_ficha(**datos)` y muestra todos los pares clave-valor.

### Actividad 3

Ordena una lista de productos por precio utilizando una lambda.

### Actividad 4

Crea un decorador que muestre:

```text
Iniciando función...
Función finalizada.
```

### Actividad 5

Crea un decorador que cuente cuántas veces se ejecuta una función.

---

[Anterior: 08. Funciones](08-funciones.md) · [Índice](README.md) · [Siguiente: 10. Trabajo con ficheros](10-ficheros.md)
