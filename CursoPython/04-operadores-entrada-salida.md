# 04. Operadores, expresiones y entrada/salida

## Objetivos

Aprender a construir expresiones, solicitar información al usuario y mostrar resultados correctamente formateados.

## 1. Expresiones

Una expresión combina valores, variables y operadores y produce un resultado.

```python
precio = 10
cantidad = 3
subtotal = precio * cantidad
```

La expresión `precio * cantidad` produce un valor que se asigna a `subtotal`.

## 2. Operadores aritméticos

| Operador | Significado | Ejemplo |
|---|---|---|
| `+` | suma | `5 + 2` |
| `-` | resta | `5 - 2` |
| `*` | multiplicación | `5 * 2` |
| `/` | división | `5 / 2` |
| `//` | división entera | `5 // 2` |
| `%` | resto | `5 % 2` |
| `**` | potencia | `5 ** 2` |

Ejemplo:

```python
print(10 / 3)
print(10 // 3)
print(10 % 3)
```

## 3. Precedencia

Python respeta un orden similar al matemático.

```python
resultado = 2 + 3 * 4
```

Resultado: `14`.

Podemos utilizar paréntesis:

```python
resultado = (2 + 3) * 4
```

Resultado: `20`.

Cuando una expresión sea compleja, los paréntesis pueden mejorar la legibilidad incluso aunque no sean estrictamente necesarios.

## 4. Operadores de comparación

| Operador | Significado |
|---|---|
| `==` | igual |
| `!=` | distinto |
| `>` | mayor |
| `<` | menor |
| `>=` | mayor o igual |
| `<=` | menor o igual |

Ejemplo:

```python
edad = 18
print(edad >= 18)
```

Produce un booleano.

## 5. Diferencia entre `=` y `==`

```python
edad = 18
```

asigna un valor.

```python
edad == 18
```

comprueba una igualdad.

## 6. Operadores lógicos

### `and`

Las dos condiciones deben cumplirse.

```python
edad = 20
tiene_carnet = True

puede_conducir = edad >= 18 and tiene_carnet
```

### `or`

Es suficiente con que una condición se cumpla.

```python
es_fin_de_semana = dia == "sábado" or dia == "domingo"
```

### `not`

Invierte un booleano.

```python
activo = True
print(not activo)
```

## 7. Operadores de asignación

```python
contador += 1
contador -= 1
precio *= 2
cantidad /= 2
```

Son formas abreviadas de expresiones como:

```python
contador = contador + 1
```

## 8. Entrada con `input()`

```python
nombre = input("Introduce tu nombre: ")
```

`input()` siempre devuelve una cadena de texto.

```python
edad = input("Edad: ")
print(type(edad))
```

## 9. Conversión al leer datos

```python
edad = int(input("Edad: "))
precio = float(input("Precio: "))
```

Si el usuario introduce un valor incompatible, se producirá una excepción. Más adelante aprenderemos a controlarla.

## 10. Salida con `print()`

```python
print("Hola")
```

Podemos mostrar varios valores:

```python
nombre = "Ana"
edad = 18
print(nombre, edad)
```

## 11. f-strings

Es la forma más cómoda de insertar valores en texto:

```python
nombre = "Ana"
edad = 18

print(f"{nombre} tiene {edad} años")
```

También podemos incluir expresiones:

```python
precio = 10
cantidad = 3
print(f"Total: {precio * cantidad}")
```

## 12. Formatear números

Dos decimales:

```python
precio = 12.5
print(f"Precio: {precio:.2f} €")
```

Porcentaje:

```python
tasa = 0.21
print(f"IVA: {tasa:.0%}")
```

Separador de miles:

```python
poblacion = 1234567
print(f"{poblacion:,}")
```

## 13. Ejemplo completo: factura sencilla

```python
IVA = 0.21

producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
impuesto = subtotal * IVA
total = subtotal + impuesto

print("\n--- RESUMEN ---")
print(f"Producto: {producto}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"IVA: {impuesto:.2f} €")
print(f"Total: {total:.2f} €")
```

## 14. Actividad principal: calculadora de compra

Solicita:

- Nombre del producto.
- Precio unitario.
- Cantidad.
- Porcentaje de descuento.

Calcula:

1. Subtotal.
2. Importe del descuento.
3. Base después del descuento.
4. IVA.
5. Total final.

Salida sugerida:

```text
========== TICKET ==========
Producto: Teclado
Cantidad: 2
Precio unitario: 25.00 €
Subtotal: 50.00 €
Descuento: 5.00 €
IVA: 9.45 €
TOTAL: 54.45 €
============================
```

---

[Anterior: 03. Variables, constantes y tipos de datos](03-variables-constantes-tipos.md) · [Índice](README.md) · [Siguiente: 05. Estructuras condicionales](05-condicionales.md)
