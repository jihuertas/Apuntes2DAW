# 03. Variables, constantes y tipos de datos

## Objetivos

Aprenderemos a almacenar información, conocer su tipo y utilizar nombres adecuados para representar los datos de un programa.

## 1. Variables

Una variable es un nombre asociado a un valor.

```python
nombre = "Ana"
edad = 18
```

En Python no es necesario declarar previamente el tipo.

```python
numero = 10
numero = 20
```

El valor puede cambiar durante la ejecución.

## 2. Asignación

El operador `=` realiza una asignación.

```python
precio = 25.50
```

No significa "es igual a" en sentido matemático. Significa: guarda `25.50` bajo el nombre `precio`.

Podemos utilizar el valor anterior:

```python
contador = 0
contador = contador + 1
```

Forma abreviada:

```python
contador += 1
```

## 3. Identificadores

Son válidos:

```python
nombre
nombre_alumno
edad2
_total
```

No son válidos:

```text
2nombre
nombre alumno
nombre-alumno
```

Python diferencia mayúsculas y minúsculas:

```python
edad = 18
Edad = 20
```

Son variables diferentes.

## 4. Convención `snake_case`

Para variables y funciones se recomienda:

```python
nombre_alumno = "Ana"
precio_total = 100
numero_intentos = 3
```

No conviene utilizar nombres sin significado:

```python
x = 19.95
```

Mejor:

```python
precio_producto = 19.95
```

## 5. Palabras reservadas

Python posee palabras con significado especial como:

```text
if
else
for
while
def
class
return
try
except
```

No pueden utilizarse como identificadores.

## 6. Constantes

Python no impide modificar un valor que consideremos constante, pero existe la convención de escribir su nombre en mayúsculas:

```python
IVA = 0.21
PI = 3.14159
MAX_ALUMNOS = 30
```

Esto comunica al resto de programadores que ese valor no debería modificarse.

## 7. Tipo `int`

Representa números enteros:

```python
edad = 18
temperatura = -3
poblacion = 150000
```

## 8. Tipo `float`

Representa números reales mediante coma flotante:

```python
precio = 19.95
altura = 1.78
```

Debe utilizarse punto como separador decimal en el código.

## 9. Tipo `str`

Representa texto:

```python
nombre = "Ana"
ciudad = 'Sevilla'
```

Una cadena puede contener números y seguir siendo texto:

```python
codigo_postal = "41001"
```

## 10. Tipo `bool`

Representa dos estados posibles:

```python
activo = True
mayor_de_edad = False
```

Los valores se escriben exactamente como `True` y `False`.

## 11. `None`

`None` representa ausencia de valor.

```python
resultado = None
```

No significa cero ni cadena vacía.

Puede utilizarse, por ejemplo, cuando todavía no conocemos un dato:

```python
fecha_baja = None
```

## 12. Consultar el tipo

```python
edad = 18
print(type(edad))
```

Salida:

```text
<class 'int'>
```

Otros ejemplos:

```python
print(type(19.95))
print(type("Hola"))
print(type(True))
print(type(None))
```

## 13. Tipado dinámico

Python permite reasignar una variable con un tipo diferente:

```python
dato = 10
dato = "diez"
```

Es posible, pero normalmente conviene mantener un significado coherente para cada variable.

## 14. Conversión de tipos

```python
numero = int("25")
precio = float("19.95")
texto = str(100)
```

Ejemplo:

```python
edad_texto = "18"
edad = int(edad_texto)
print(edad + 1)
```

No todas las conversiones son válidas:

```python
int("hola")
```

provocará un error.

## 15. Cadenas de texto

### Longitud

```python
nombre = "Python"
print(len(nombre))
```

### Acceso por posición

```python
print(nombre[0])
print(nombre[-1])
```

Los índices comienzan en cero.

### Slicing

```python
texto = "Python"
print(texto[0:3])
```

Resultado:

```text
Pyt
```

### Métodos útiles

```python
texto.upper()
texto.lower()
texto.strip()
texto.replace("Py", "My")
texto.startswith("Py")
texto.endswith("on")
```

## 16. Inmutabilidad de `str`

Las cadenas no se modifican internamente.

```python
nombre = "ana"
nombre.upper()
print(nombre)
```

Sigue mostrando `ana`.

Para conservar el nuevo valor:

```python
nombre = nombre.upper()
```

## 17. Asignación múltiple

```python
x, y = 10, 20
```

También podemos intercambiar valores:

```python
x, y = y, x
```

## 18. Actividades

### Actividad 1

Crea variables para representar:

- Nombre de un alumno.
- Edad.
- Nota media.
- Si está matriculado.
- Fecha de baja, inicialmente desconocida.

Muestra el tipo de cada variable.

### Actividad 2

Define las constantes:

```text
IVA = 21 %
DESCUENTO_MAXIMO = 30 %
MAX_INTENTOS = 3
```

Utiliza nombres adecuados y valores apropiados para realizar cálculos posteriormente.

### Actividad 3

Dada una variable:

```python
nombre_completo = "  ana garcía  "
```

consigue mostrar:

```text
Ana García
```

---

[Anterior: 02. Entorno de desarrollo](02-entorno-desarrollo.md) · [Índice](README.md) · [Siguiente: 04. Operadores, expresiones y entrada/salida](04-operadores-entrada-salida.md)
