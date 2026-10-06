# 🐍 Boletín de ejercicios de Python

En este boletín se trabajarán de forma práctica los principales contenidos vistos hasta ahora en el curso:

- Bucles y estructuras condicionales.
- Listas.
- Diccionarios.
- Listas de diccionarios.
- Funciones.
- Lectura y escritura de ficheros.
- Ficheros TXT, CSV y JSON.
- Programación orientada a objetos.

> 💡 **Recomendación:** intenta dividir los programas más complejos en funciones y evita repetir código.

---

## Ejercicio 1. Control de ocupación de un aparcamiento

Un aparcamiento dispone de **20 plazas**. Durante el día se han registrado los siguientes movimientos:

```python
movimientos = [
    "entrada", "entrada", "entrada", "salida",
    "entrada", "entrada", "salida", "salida",
    "entrada", "entrada", "entrada", "entrada"
]
```

Realiza un programa que recorra la lista y vaya calculando en cada momento el número de vehículos que hay dentro.

El programa deberá:

1. Procesar todos los movimientos en el orden en el que aparecen.
2. Impedir que el número de vehículos sea menor que 0.
3. Impedir nuevas entradas si el aparcamiento está completo.
4. Mostrar después de cada movimiento:
   - Número de vehículos.
   - Número de plazas libres.
5. Indicar cuál fue el **número máximo de vehículos simultáneos**.
6. Contar cuántas entradas y salidas se realizaron correctamente.
7. Mostrar al final el **porcentaje de ocupación** del aparcamiento.

### Ampliación

Permite que, una vez procesada la lista inicial, el usuario pueda introducir nuevos movimientos:

```text
entrada
salida
fin
```

El programa terminará cuando se introduzca `fin`.

---

## Ejercicio 2. Análisis de ventas semanales

Disponemos de dos listas con los días de la semana y las ventas realizadas:

```python
dias = [
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
]

ventas = [1250, 980, 1430, 2100, 1750, 900, 2350]
```

Crea un programa que:

1. Calcule la **venta total de la semana**.
2. Calcule la **media diaria de ventas**.
3. Muestre los días cuyas ventas superaron la media.
4. Indique:
   - Día con mayor número de ventas.
   - Día con menor número de ventas.
5. Cuente cuántos días se superaron los **1.500 €**.
6. Calcule qué porcentaje de las ventas semanales corresponde al mejor día.
7. Muestre los días ordenados de **mayor a menor venta** sin modificar las listas originales.

> **Restricción:** no utilices `lambda`.

---

# Diccionarios

## Ejercicio 3. Gestión de puntuaciones de un videojuego

Disponemos de un diccionario que almacena jugadores y sus puntuaciones:

```python
puntuaciones = {
    "Mario": 1250,
    "Lucía": 890,
    "Carlos": 1420,
    "Ana": 1100
}
```

Crea un programa con el siguiente menú:

```text
1. Añadir jugador
2. Modificar puntuación
3. Eliminar jugador
4. Consultar jugador
5. Mostrar mejor jugador
6. Mostrar jugadores que superan una puntuación
7. Mostrar puntuación media
8. Salir
```

El programa deberá:

- Evitar jugadores duplicados.
- Comprobar que un jugador existe antes de modificarlo o eliminarlo.
- Mostrar el jugador con mayor puntuación.
- Permitir introducir una puntuación y mostrar todos los jugadores que la superen.
- Calcular la puntuación media de todos los jugadores.

El menú deberá repetirse hasta seleccionar la opción **Salir**.

---

## Ejercicio 4. Traductor básico

Crea un diccionario español-inglés:

```python
diccionario = {
    "casa": "house",
    "coche": "car",
    "libro": "book",
    "mesa": "table"
}
```

El programa deberá mostrar un menú que permita:

1. Traducir una palabra.
2. Añadir una nueva traducción.
3. Modificar una traducción existente.
4. Eliminar una palabra.
5. Mostrar todas las palabras ordenadas alfabéticamente.
6. Traducir una frase.
7. Salir.

Para la traducción de frases, el programa deberá sustituir únicamente las palabras que encuentre en el diccionario.

Por ejemplo:

```text
Introduce una frase: la casa tiene una mesa
```

Resultado:

```text
la house tiene una table
```

Las palabras que no estén en el diccionario deberán mantenerse sin modificar.

---

# Listas de diccionarios

## Ejercicio 5. Catálogo de películas

Las películas se almacenarán utilizando una **lista de diccionarios**:

```python
peliculas = [
    {
        "titulo": "Matrix",
        "anio": 1999,
        "genero": "Ciencia ficción",
        "puntuacion": 8.7
    },
    {
        "titulo": "Gladiator",
        "anio": 2000,
        "genero": "Drama",
        "puntuacion": 8.5
    }
]
```

Crea un programa que permita:

1. Añadir una película.
2. Buscar una película por título.
3. Mostrar todas las películas.
4. Mostrar las películas de un género determinado.
5. Mostrar películas posteriores a un año indicado.
6. Calcular la puntuación media de todas las películas.
7. Mostrar la película mejor valorada.
8. Eliminar una película.
9. Salir.

Cada película deberá almacenarse como un nuevo diccionario dentro de la lista.

### Requisito

Organiza las principales operaciones utilizando **funciones**.

Por ejemplo:

```python
def buscar_pelicula(peliculas, titulo):
    # ...
```

---

## Ejercicio 6. Gestión de pedidos de una tienda

Los pedidos de una tienda se almacenan utilizando una lista de diccionarios:

```python
pedidos = [
    {
        "numero": 101,
        "cliente": "Ana",
        "importe": 125.50,
        "estado": "pendiente"
    },
    {
        "numero": 102,
        "cliente": "Luis",
        "importe": 89.90,
        "estado": "enviado"
    }
]
```

Los estados permitidos para un pedido son:

```text
pendiente
enviado
entregado
cancelado
```

Crea un programa que permita:

1. Registrar un nuevo pedido.
2. Buscar un pedido por número.
3. Cambiar el estado de un pedido.
4. Mostrar todos los pedidos pendientes.
5. Mostrar todos los pedidos de un determinado cliente.
6. Calcular el importe total de los pedidos.
7. Obtener el pedido de mayor importe.
8. Mostrar cuántos pedidos existen en cada estado.
9. Salir.

El programa deberá comprobar que:

- No existan dos pedidos con el mismo número.
- El estado introducido sea válido.
- El pedido exista antes de modificarlo.

Organiza el programa utilizando **funciones**.

---

# Ficheros

## Ejercicio 7. Analizador de registros de acceso

Disponemos de un fichero llamado `accesos.txt` con el siguiente formato:

```text
ana;08:15
luis;08:22
marta;08:35
ana;10:20
luis;11:15
ana;12:40
```

Cada línea representa el nombre de un usuario y la hora en la que ha accedido al sistema.

Crea un programa que:

1. Lea el fichero completo.
2. Cuente el número total de accesos.
3. Obtenga los distintos usuarios que aparecen en el fichero.
4. Cuente cuántos accesos ha realizado cada usuario.
5. Determine qué usuario ha realizado más accesos.
6. Genere un fichero llamado `resumen.txt`.

El fichero generado podría tener un formato similar a:

```text
RESUMEN DE ACCESOS
------------------

Total de accesos: 6
Usuarios diferentes: 3

ana: 3 accesos
luis: 2 accesos
marta: 1 acceso

Usuario con más accesos: ana
```

> El programa no debe conocer previamente cuántos usuarios existen.

---

## Ejercicio 8. Inventario con CSV y JSON

Disponemos de un fichero llamado `productos.csv`:

```csv
codigo,nombre,precio,stock
P001,Teclado,25.90,8
P002,Raton,12.50,15
P003,Monitor,199.90,4
P004,Webcam,45.50,3
```

Crea un programa que:

1. Lea los productos del fichero CSV.
2. Convierta cada producto en un diccionario.
3. Almacene todos los productos en una lista.
4. Muestre todos los productos.
5. Muestre los productos cuyo stock sea inferior a 5 unidades.
6. Calcule el **valor total del inventario**.

Para cada producto:

```text
valor = precio × stock
```

El programa también deberá permitir:

7. Buscar un producto por código.
8. Modificar su stock.
9. Guardar todos los datos actualizados en un fichero:

```text
productos.json
```

El fichero JSON deberá conservar todos los datos de los productos.

Ejemplo:

```json
[
    {
        "codigo": "P001",
        "nombre": "Teclado",
        "precio": 25.90,
        "stock": 8
    }
]
```

---

# Programación orientada a objetos

## Ejercicio 9. Gestión de cuentas bancarias

Crea una clase llamada:

```python
CuentaBancaria
```

con los siguientes atributos:

```text
numero_cuenta
titular
saldo
```

Implementa un constructor que permita crear una cuenta indicando sus datos.

La clase deberá disponer, al menos, de los siguientes métodos:

```python
ingresar(cantidad)
retirar(cantidad)
mostrar_saldo()
mostrar_datos()
```

Ten en cuenta que:

- No se pueden ingresar cantidades negativas.
- No se pueden retirar cantidades negativas.
- No se puede retirar una cantidad superior al saldo disponible.

A continuación:

1. Crea al menos **5 cuentas bancarias**.
2. Almacénalas en una lista.
3. Realiza diferentes ingresos y retiradas.
4. Muestra los datos de todas las cuentas.
5. Obtén la cuenta con mayor saldo.
6. Calcula el dinero total almacenado entre todas las cuentas.

### Ampliación

Añade un método:

```python
transferir(destino, cantidad)
```

que permita transferir dinero entre dos objetos `CuentaBancaria`.

La transferencia solamente podrá realizarse si la cuenta de origen dispone de saldo suficiente.

---

## Ejercicio 10. Empresa de alquiler de vehículos

Crea una clase:

```python
Vehiculo
```

con los atributos:

```text
matricula
marca
modelo
precio_dia
disponible
```

El atributo `disponible` deberá indicar si el vehículo puede ser alquilado.

Implementa los métodos:

```python
alquilar()
devolver()
mostrar()
calcular_precio(dias)
```

A continuación, crea una segunda clase:

```python
EmpresaAlquiler
```

que tendrá como atributo una lista de objetos `Vehiculo`.

La clase deberá proporcionar métodos para:

1. Añadir un vehículo.
2. Buscar un vehículo por matrícula.
3. Mostrar todos los vehículos.
4. Mostrar únicamente los vehículos disponibles.
5. Alquilar un vehículo.
6. Devolver un vehículo.
7. Calcular el precio de un alquiler indicando el número de días.
8. Mostrar el vehículo con el precio diario más alto.

Finalmente, crea un programa principal con el siguiente menú:

```text
1. Añadir vehículo
2. Mostrar vehículos
3. Mostrar vehículos disponibles
4. Alquilar vehículo
5. Devolver vehículo
6. Consultar precio de alquiler
7. Salir
```

El menú deberá repetirse hasta que el usuario seleccione **Salir**.

---

## Recomendaciones generales

Antes de comenzar cada ejercicio:

1. Analiza qué estructuras de datos necesitas.
2. Divide el problema en tareas más pequeñas.
3. Utiliza funciones cuando una operación pueda separarse del programa principal.
4. Utiliza nombres descriptivos para variables, funciones, clases y métodos.
5. Controla los posibles errores en los datos introducidos por el usuario.
6. Prueba el programa con diferentes datos antes de darlo por terminado.

> **Importante:** no se busca únicamente que el programa funcione. Intenta que el código sea legible, esté bien estructurado y evite repeticiones innecesarias.
