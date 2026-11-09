# 12. Excepciones

## Objetivos

Aprender a detectar y gestionar situaciones anómalas sin provocar la finalización inesperada del programa.

## 1. ¿Qué es una excepción?

Una excepción es un evento que interrumpe el flujo normal de ejecución.

Ejemplo:

```python
edad = int(input("Edad: "))
```

Si el usuario introduce:

```text
hola
```

Python no puede convertirlo a entero y lanza `ValueError`.

## 2. Excepciones comunes

### `ValueError`

Valor correcto en tipo general, pero contenido no válido para la operación.

```python
int("hola")
```

### `TypeError`

Operación aplicada a tipos incompatibles.

```python
"10" + 5
```

### `ZeroDivisionError`

```python
10 / 0
```

### `IndexError`

```python
lista = [1, 2]
print(lista[10])
```

### `KeyError`

```python
alumno = {"nombre": "Ana"}
print(alumno["edad"])
```

### `FileNotFoundError`

```python
open("no-existe.txt")
```

## 3. `try` / `except`

```python
try:
    edad = int(input("Edad: "))
except ValueError:
    print("Debes introducir un número entero")
```

El bloque `except` solo se ejecuta si aparece esa excepción.

## 4. Capturar varias excepciones

```python
try:
    numero = int(input("Número: "))
    resultado = 100 / numero
except ValueError:
    print("Debes introducir un número")
except ZeroDivisionError:
    print("No puedes utilizar cero")
```

## 5. Varias excepciones en un mismo bloque

```python
try:
    ...
except (ValueError, TypeError):
    print("Datos incorrectos")
```

## 6. Obtener información de la excepción

```python
try:
    numero = int("abc")
except ValueError as error:
    print(f"Error: {error}")
```

Puede resultar útil para registrar información técnica.

## 7. Evitar `except` demasiado amplio

No es recomendable:

```python
try:
    ...
except:
    print("Error")
```

Oculta cualquier problema, incluso errores de programación.

Es preferible capturar excepciones concretas.

## 8. `else`

Se ejecuta cuando el `try` termina sin excepción.

```python
try:
    edad = int(input("Edad: "))
except ValueError:
    print("Edad incorrecta")
else:
    print(f"Edad válida: {edad}")
```

## 9. `finally`

Se ejecuta siempre.

```python
try:
    print("Procesando")
finally:
    print("Finalizando")
```

Es útil para liberar determinados recursos, aunque con archivos solemos utilizar `with`.

## 10. Lanzar excepciones con `raise`

Nosotros también podemos detectar situaciones incorrectas.

```python
def validar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10")
```

Uso:

```python
try:
    validar_nota(15)
except ValueError as error:
    print(error)
```

## 11. Validación frente a excepción

No todos los errores de usuario necesitan resolverse mediante excepciones.

Por ejemplo:

```python
if opcion not in ("1", "2", "3"):
    print("Opción no válida")
```

Pero cuando una operación puede fallar naturalmente, `try` resulta apropiado.

## 12. Ejemplo robusto para leer un entero

```python
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes introducir un número entero")
```

Uso:

```python
edad = pedir_entero("Edad: ")
```

## 13. JSON incorrecto

```python
import json

try:
    with open("datos.json", encoding="utf-8") as fichero:
        datos = json.load(fichero)
except FileNotFoundError:
    datos = []
except json.JSONDecodeError:
    print("El fichero JSON está dañado")
    datos = []
```

## 14. Excepciones personalizadas

En aplicaciones mayores podemos crear excepciones propias.

```python
class NotaIncorrectaError(Exception):
    pass
```

```python
def validar_nota(nota):
    if not 0 <= nota <= 10:
        raise NotaIncorrectaError("Nota fuera de rango")
```

No siempre es necesario, pero permite expresar mejor errores propios del dominio.

## 15. Práctica principal

Haz resistente a errores la aplicación de alumnado.

Debe controlar:

- Introducción de una nota no numérica.
- Nota fuera del rango 0-10.
- Alumno inexistente.
- Archivo JSON inexistente.
- JSON mal formado.
- Opción de menú desconocida.

El programa no debería cerrarse inesperadamente por ninguno de esos errores previsibles.

---

[Anterior: 11. JSON y CSV](11-json-csv.md) · [Índice](README.md) · [Siguiente: 13. Módulos y paquetes](13-modulos-paquetes.md)
