# 06. Bucles

## Objetivos

Aprender a repetir instrucciones utilizando `while` y `for`, controlar la finalización de los bucles y reconocer patrones como contadores y acumuladores.

## 1. ¿Por qué necesitamos bucles?

Sin bucles, para mostrar los números del 1 al 5 escribiríamos:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Con un bucle podemos expresar la repetición de forma general.

## 2. Bucle `while`

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Funcionamiento:

1. Se evalúa `contador <= 5`.
2. Si es verdadero, se ejecuta el bloque.
3. Se vuelve a evaluar la condición.
4. Termina cuando la condición es falsa.

## 3. Bucle infinito

```python
contador = 1

while contador <= 5:
    print(contador)
```

`contador` nunca cambia, por lo que la condición siempre será verdadera.

## 4. `while True`

Puede utilizarse de forma deliberada cuando existe una salida explícita:

```python
while True:
    opcion = input("Escribe 'salir': ")

    if opcion == "salir":
        break
```

## 5. Contadores

```python
contador = 0

while contador < 10:
    contador += 1
```

Un contador registra cuántas veces ocurre algo.

## 6. Acumuladores

```python
total = 0

for numero in range(1, 6):
    total += numero

print(total)
```

Un acumulador mantiene un resultado parcial.

## 7. Bucle `for`

Python utiliza `for` para recorrer elementos de una secuencia o iterable.

```python
for numero in range(5):
    print(numero)
```

Salida:

```text
0
1
2
3
4
```

## 8. `range()`

### Un argumento

```python
range(5)
```

Genera valores desde `0` hasta `4`.

### Inicio y fin

```python
range(1, 6)
```

Genera `1, 2, 3, 4, 5`.

### Paso

```python
range(0, 11, 2)
```

Genera números pares.

### Descendente

```python
range(10, 0, -1)
```

## 9. Recorrer cadenas

```python
for letra in "Python":
    print(letra)
```

Esto introduce una idea fundamental: `for` no sirve únicamente para contar.

## 10. `break`

Finaliza el bucle actual.

```python
for numero in range(1, 100):
    if numero == 7:
        break
    print(numero)
```

## 11. `continue`

Omite el resto de la iteración actual.

```python
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)
```

## 12. Bucles anidados

```python
for fila in range(3):
    for columna in range(3):
        print(f"{fila=}, {columna=}")
```

Cada iteración del bucle exterior ejecuta completamente el interior.

## 13. Tabla de multiplicar

```python
numero = int(input("Número: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
```

## 14. Menús repetitivos

Los bucles permiten mantener una aplicación funcionando hasta que el usuario decida salir.

```python
while True:
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        print("Hola")
    elif opcion == "0":
        break
    else:
        print("Opción no válida")
```

## 15. `else` en bucles

Python permite asociar `else` a un bucle. Se ejecuta si el bucle termina sin utilizar `break`.

```python
numero_buscado = 7

for numero in range(10):
    if numero == numero_buscado:
        print("Encontrado")
        break
else:
    print("No encontrado")
```

No es imprescindible al principio, pero conviene conocerlo.

## 16. Práctica: adivina el número

Objetivos:

1. Generar un número aleatorio.
2. Solicitar intentos al usuario.
3. Informar si el número buscado es mayor o menor.
4. Contar intentos.
5. Finalizar cuando se acierte.

Base:

```python
import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    numero = int(input("Introduce un número entre 1 y 100: "))
    intentos += 1

    if numero < numero_secreto:
        print("El número secreto es mayor")
    elif numero > numero_secreto:
        print("El número secreto es menor")
    else:
        print(f"Correcto. Has necesitado {intentos} intentos.")
        break
```

## 17. Actividades adicionales

- Mostrar todos los números pares entre 1 y 100.
- Calcular la suma de los números del 1 al 100.
- Pedir números hasta que el usuario introduzca `0` y mostrar su suma.
- Crear todas las tablas de multiplicar del 1 al 10 utilizando bucles anidados.

---

[Anterior: 05. Estructuras condicionales](05-condicionales.md) · [Índice](README.md) · [Siguiente: 07. Listas, tuplas, conjuntos y diccionarios](07-colecciones.md)
