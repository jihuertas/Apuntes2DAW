# 05. Estructuras condicionales

## Objetivos

Aprender a modificar el flujo de ejecución de un programa tomando decisiones en función de condiciones.

## 1. Flujo secuencial

Hasta ahora las instrucciones se ejecutan en orden:

```python
nombre = input("Nombre: ")
print(f"Hola {nombre}")
print("Fin")
```

Las estructuras condicionales permiten ejecutar determinadas instrucciones solo cuando se cumple una condición.

## 2. `if`

```python
edad = 20

if edad >= 18:
    print("Mayor de edad")
```

La expresión situada después de `if` debe producir un valor booleano.

## 3. La indentación

Python utiliza indentación para delimitar bloques.

```python
if edad >= 18:
    print("Acceso permitido")
    print("Puede continuar")

print("Fin")
```

Las dos primeras instrucciones pertenecen al `if`; la última no.

Se recomienda utilizar cuatro espacios por nivel.

## 4. `if` / `else`

```python
nota = 6.5

if nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

Solo se ejecutará uno de los dos bloques.

## 5. `if` / `elif` / `else`

```python
nota = 8

if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
```

Python evalúa las condiciones de arriba hacia abajo y se detiene en la primera verdadera.

## 6. Importancia del orden

Este código es incorrecto conceptualmente:

```python
if nota >= 5:
    print("Aprobado")
elif nota >= 9:
    print("Sobresaliente")
```

Una nota de 10 cumple primero `nota >= 5`, por lo que nunca llegará al segundo bloque.

Una forma correcta:

```python
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

## 7. Condiciones compuestas

```python
edad = 20
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir")
```

Con `or`:

```python
if dia == "sábado" or dia == "domingo":
    print("Fin de semana")
```

Con `not`:

```python
if not bloqueado:
    print("Acceso permitido")
```

## 8. Condicionales anidados

```python
usuario = "admin"
password = "1234"

if usuario == "admin":
    if password == "1234":
        print("Acceso correcto")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")
```

Aunque son válidos, un exceso de anidamiento puede dificultar la lectura.

## 9. Valores truthy y falsy

Python interpreta algunos valores como falsos:

- `False`
- `None`
- `0`
- `0.0`
- `""`
- colecciones vacías

Ejemplo:

```python
nombre = input("Nombre: ")

if nombre:
    print(f"Hola {nombre}")
else:
    print("No has escrito ningún nombre")
```

## 10. Operador ternario

Permite elegir entre dos valores en una única expresión.

```python
nota = 7
resultado = "Aprobado" if nota >= 5 else "Suspenso"
```

Debe utilizarse solo cuando mejora la claridad.

## 11. Pertenencia con `in`

```python
opcion = input("Opción: ")

if opcion in ("1", "2", "3"):
    print("Opción válida")
```

También funciona con cadenas y otras colecciones.

## 12. Ejemplo: control de acceso

```python
EDAD_MINIMA = 18

usuario = input("Usuario: ").strip()
password = input("Contraseña: ")
edad = int(input("Edad: "))

if usuario != "admin":
    print("Usuario incorrecto")
elif password != "python123":
    print("Contraseña incorrecta")
elif edad < EDAD_MINIMA:
    print("No cumples la edad mínima")
else:
    print("Acceso permitido")
```

## 13. Actividades

### Actividad 1: clasificación de una nota

Solicita una nota de 0 a 10 y muestra:

- Suspenso.
- Suficiente.
- Bien.
- Notable.
- Sobresaliente.

### Actividad 2: año bisiesto

Investiga las reglas y crea un programa que determine si un año es bisiesto.

### Actividad 3: tarifa de entrada

Calcula el precio de una entrada según edad y condición de estudiante.

---

[Anterior: 04. Operadores, expresiones y entrada/salida](04-operadores-entrada-salida.md) · [Índice](README.md) · [Siguiente: 06. Bucles](06-bucles.md)
