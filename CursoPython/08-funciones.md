# 08. Funciones

## Objetivos

Aprender a dividir un programa en unidades pequeñas, reutilizables y fáciles de probar.

## 1. Problema del código repetido

```python
print("================")
print("GESTIÓN ALUMNOS")
print("================")
```

Si necesitamos este encabezado varias veces, duplicar código dificulta el mantenimiento.

Podemos crear una función.

## 2. Definir una función

```python
def mostrar_cabecera():
    print("================")
    print("GESTIÓN ALUMNOS")
    print("================")
```

Ejecutarla:

```python
mostrar_cabecera()
```

## 3. Parámetros

```python
def saludar(nombre):
    print(f"Hola {nombre}")
```

Uso:

```python
saludar("Ana")
saludar("Luis")
```

`nombre` es un parámetro; `"Ana"` es un argumento.

## 4. Varios parámetros

```python
def calcular_total(precio, cantidad):
    print(precio * cantidad)
```

```python
calcular_total(19.95, 3)
```

## 5. `return`

Una función puede devolver un resultado:

```python
def sumar(a, b):
    return a + b
```

Uso:

```python
resultado = sumar(5, 3)
print(resultado)
```

## 6. `print()` no sustituye a `return`

```python
def sumar_mal(a, b):
    print(a + b)
```

La función muestra el resultado, pero no lo devuelve.

```python
resultado = sumar_mal(2, 3)
print(resultado)
```

Después de imprimir `5`, veremos `None`.

Mejor:

```python
def sumar(a, b):
    return a + b
```

Esto permite reutilizar el resultado.

## 7. Retorno temprano

```python
def dividir(a, b):
    if b == 0:
        return None

    return a / b
```

Al ejecutar `return`, la función termina.

## 8. Parámetros por defecto

```python
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje} {nombre}")
```

```python
saludar("Ana")
saludar("Ana", "Buenos días")
```

## 9. Argumentos nombrados

```python
saludar(nombre="Ana", mensaje="Buenos días")
```

Esto mejora la claridad cuando una función tiene varios parámetros.

## 10. Variables locales

```python
def calcular():
    resultado = 10 + 5
    print(resultado)
```

`resultado` solo existe dentro de la función.

## 11. Ámbito global

```python
IVA = 0.21

def calcular_iva(precio):
    return precio * IVA
```

Las constantes globales pueden tener sentido.

En cambio, modificar variables globales desde funciones suele complicar el programa.

## 12. Evitar efectos secundarios innecesarios

Preferible:

```python
def calcular_media(notas):
    return sum(notas) / len(notas)
```

frente a una función que dependa de una lista global escondida.

## 13. Documentar funciones

Docstring:

```python
def calcular_media(notas):
    """Devuelve la media aritmética de una colección de notas."""
    return sum(notas) / len(notas)
```

Podemos consultar:

```python
help(calcular_media)
```

## 14. Anotaciones de tipo

Python permite expresar el tipo esperado sin convertirlo en obligatorio en tiempo de ejecución.

```python
def sumar(a: float, b: float) -> float:
    return a + b
```

Con colecciones:

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)
```

Las anotaciones ayudan al editor, a las herramientas de análisis y a la documentación.

## 15. Funciones pequeñas

Una función debería realizar una tarea clara.

En lugar de:

```python
def gestionar_todo():
    ...
```

podemos tener:

```python
def mostrar_menu():
    ...

def crear_alumno():
    ...

def buscar_alumno():
    ...

def calcular_media():
    ...
```

## 16. Refactorización de la práctica anterior

Antes:

```python
if opcion == "1":
    nombre = input("Nombre: ")
    alumnos.append({"nombre": nombre, "notas": []})
```

Después:

```python
def añadir_alumno(alumnos):
    nombre = input("Nombre: ").strip()
    alumnos.append({"nombre": nombre, "notas": []})
```

Y en el menú:

```python
if opcion == "1":
    añadir_alumno(alumnos)
```

## 17. Actividad principal

Refactoriza la aplicación de gestión de alumnado para incluir al menos:

```python
def mostrar_menu():
    ...

def añadir_alumno(alumnos):
    ...

def buscar_alumno(alumnos, nombre):
    ...

def eliminar_alumno(alumnos, nombre):
    ...

def añadir_nota(alumno, nota):
    ...

def calcular_media(alumno):
    ...

def listar_alumnos(alumnos):
    ...

def main():
    ...
```

El programa debería iniciarse mediante:

```python
if __name__ == "__main__":
    main()
```

El significado de esta construcción se estudiará con más detalle en el tema de módulos.

---

[Anterior: 07. Listas, tuplas, conjuntos y diccionarios](07-colecciones.md) · [Índice](README.md) · [Siguiente: 09. *args, **kwargs, lambda y decoradores](09-funciones-avanzadas.md)
