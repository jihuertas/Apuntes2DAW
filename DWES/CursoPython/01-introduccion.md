# 01. Introducción a Python

## Objetivos

En este tema aprenderemos qué significa programar, qué es un algoritmo, qué papel desempeña un lenguaje de programación y por qué Python es una herramienta adecuada para comenzar a programar.

Al finalizar deberías ser capaz de:

- Explicar qué es un programa y qué es un algoritmo.
- Diferenciar código fuente, intérprete y ejecución.
- Reconocer algunas características fundamentales de Python.
- Ejecutar instrucciones sencillas.
- Utilizar `print()` y comentarios.

## 1. ¿Qué es programar?

Programar consiste en describir, de manera suficientemente precisa, una secuencia de instrucciones que un ordenador pueda ejecutar.

Un programa suele realizar una combinación de estas tareas:

1. Obtener información.
2. Almacenar datos.
3. Realizar cálculos.
4. Tomar decisiones.
5. Repetir operaciones.
6. Mostrar o guardar resultados.

Ejemplo:

```python
print("Hola mundo")
```

La instrucción anterior pide a Python que muestre un mensaje por pantalla.

## 2. Algoritmos

Antes de escribir código es frecuente describir la solución como una secuencia de pasos. Esa secuencia se denomina **algoritmo**.

Ejemplo: calcular la media de tres notas.

```text
1. Leer la primera nota.
2. Leer la segunda nota.
3. Leer la tercera nota.
4. Sumar las tres notas.
5. Dividir el resultado entre tres.
6. Mostrar la media.
```

Una posible implementación en Python sería:

```python
nota1 = 7
nota2 = 8
nota3 = 6

media = (nota1 + nota2 + nota3) / 3
print(media)
```

Es importante distinguir entre **resolver el problema** y **escribir la solución en un lenguaje concreto**. Un mismo algoritmo puede implementarse en Python, Java, JavaScript o cualquier otro lenguaje adecuado.

## 3. Lenguajes de programación

Un lenguaje de programación define:

- Una sintaxis: cómo deben escribirse las instrucciones.
- Un conjunto de palabras reservadas.
- Un conjunto de tipos de datos.
- Reglas para combinar expresiones e instrucciones.
- Herramientas para estructurar programas.

Algunos lenguajes conocidos son Python, Java, JavaScript, C, C++, C#, PHP, Kotlin o Swift.

## 4. Código fuente e intérprete

El archivo que escribimos contiene **código fuente**. El ordenador no ejecuta directamente ese texto: necesita un programa que lo procese.

Desde el punto de vista del programador, Python se utiliza normalmente mediante un **intérprete**.

Si tenemos un archivo:

```text
programa.py
```

podemos ejecutarlo con:

```bash
python programa.py
```

## 5. ¿Qué es Python?

Python es un lenguaje de programación de propósito general caracterizado por una sintaxis clara y una gran cantidad de bibliotecas disponibles.

Entre sus características destacan:

- Es multiplataforma.
- Tiene tipado dinámico.
- Permite programación procedural, funcional y orientada a objetos.
- Cuenta con una amplia biblioteca estándar.
- Dispone de un gran ecosistema de paquetes externos.
- Se utiliza tanto en enseñanza como en proyectos profesionales.

## 6. ¿Para qué se utiliza Python?

### Desarrollo web

Frameworks como:

- Django.
- Flask.
- FastAPI.

### Automatización

Python puede utilizarse para:

- Renombrar archivos.
- Procesar hojas de cálculo.
- Crear informes.
- Automatizar tareas administrativas.
- Consumir APIs.

### Datos e inteligencia artificial

Bibliotecas habituales:

- NumPy.
- Pandas.
- Matplotlib.
- scikit-learn.
- PyTorch.

### Administración de sistemas

También resulta útil para crear scripts, procesar registros, realizar copias de seguridad o automatizar despliegues.

## 7. Nuestro primer programa

```python
print("Hola mundo")
```

Podemos añadir más instrucciones:

```python
print("Hola")
print("Estoy aprendiendo Python")
print("Este es mi primer programa")
```

Python ejecutará las instrucciones, por defecto, de arriba hacia abajo.

## 8. Python también puede calcular

```python
print(2 + 3)
print(10 * 5)
print(2 ** 8)
```

Salida:

```text
5
50
256
```

## 9. Texto frente a expresiones

Observa la diferencia:

```python
print(2 + 3)
print("2 + 3")
```

El primer caso evalúa la expresión y muestra `5`. El segundo muestra literalmente el texto `2 + 3`.

## 10. Comentarios

Los comentarios sirven para documentar el código y no se ejecutan.

```python
# Este programa muestra un saludo
print("Hola")
```

También pueden aparecer al final de una línea:

```python
edad = 18  # Edad del usuario
```

Conviene evitar comentarios que simplemente repitan lo evidente.

Mal ejemplo:

```python
edad = 18  # Asignamos 18 a edad
```

Mejor:

```python
EDAD_MINIMA = 18  # Edad mínima exigida para acceder
```

## 11. Errores iniciales

### Error de sintaxis

```python
print("Hola"
```

El programa no respeta la sintaxis de Python.

### Error de ejecución

```python
print(numero)
```

Si `numero` no existe, Python generará un error al ejecutar esa línea.

### Error lógico

```python
precio = 100
iva = precio * 21
```

El programa puede ejecutarse, pero el cálculo es incorrecto si pretendíamos calcular un 21 %.

## 12. Actividades

### Actividad 1

Crea un programa que muestre:

```text
============================
     MI PRIMER PROGRAMA
============================
Nombre: Ana
Curso: 2º DAW
Lenguaje: Python
============================
```

### Actividad 2

Muestra el resultado de:

- `15 + 7`
- `20 - 8`
- `6 * 9`
- `100 / 4`
- `2 ** 10`

### Actividad 3

Escribe un algoritmo, sin programarlo todavía, para calcular el precio final de un producto después de aplicar un descuento.

---

[Anterior: Índice](README.md) · [Índice](README.md) · [Siguiente: 02. Entorno de desarrollo](02-entorno-desarrollo.md)
