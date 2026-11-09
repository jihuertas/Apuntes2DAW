# 15. Programación orientada a objetos: herencia y composición

## Objetivos

Aprender a relacionar clases mediante herencia y composición y comprender cuándo conviene utilizar cada mecanismo.

# Herencia

## 1. Concepto

La herencia permite crear una clase a partir de otra.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
```

Clase derivada:

```python
class Alumno(Persona):
    pass
```

Ahora `Alumno` hereda el comportamiento de `Persona`.

```python
ana = Alumno("Ana")
print(ana.nombre)
```

## 2. Añadir atributos en la subclase

```python
class Alumno(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)
        self.curso = curso
```

## 3. `super()`

```python
super().__init__(nombre)
```

Permite ejecutar el constructor de la clase base sin repetir su código.

## 4. Añadir comportamiento específico

```python
class Alumno(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)
        self.curso = curso
        self.notas = []

    def añadir_nota(self, nota):
        self.notas.append(nota)
```

## 5. Sobrescritura de métodos

```python
class Persona:
    def descripcion(self):
        return f"Persona: {self.nombre}"


class Alumno(Persona):
    def descripcion(self):
        return f"Alumno: {self.nombre} - {self.curso}"
```

La subclase proporciona su propia implementación.

# Polimorfismo

## 6. Mismo mensaje, distinto comportamiento

```python
class Alumno(Persona):
    def tipo(self):
        return "Alumno"


class Profesor(Persona):
    def tipo(self):
        return "Profesor"
```

```python
personas = [
    Alumno("Ana", "2º DAW"),
    Profesor("Luis"),
]

for persona in personas:
    print(persona.tipo())
```

El mismo método puede producir comportamiento distinto dependiendo del objeto.

## 7. `isinstance()`

```python
if isinstance(persona, Alumno):
    print("Es un alumno")
```

También reconoce herencia:

```python
isinstance(ana, Persona)
```

será verdadero.

# Composición

## 8. Concepto

La composición representa una relación "tiene un" o "contiene".

```python
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
```

Un `Curso` contiene objetos `Alumno`.

```python
def añadir_alumno(self, alumno):
    self.alumnos.append(alumno)
```

## 9. Ejemplo

```python
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def añadir_alumno(self, alumno):
        self.alumnos.append(alumno)

    def listar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno)
```

Uso:

```python
curso = Curso("2º DAW")
curso.añadir_alumno(Alumno("Ana", "2º DAW"))
curso.añadir_alumno(Alumno("Luis", "2º DAW"))
curso.listar_alumnos()
```

## 10. Herencia frente a composición

Pregunta útil:

### "Es un"

```text
Alumno es una Persona
Profesor es una Persona
```

Puede indicar herencia.

### "Tiene un" o "contiene"

```text
Curso tiene Alumnos
Biblioteca tiene Libros
Pedido contiene Líneas de pedido
```

Suele indicar composición.

No debemos utilizar herencia simplemente para reutilizar código si la relación conceptual no existe.

# Clases abstractas

## 11. Idea general

En diseños más avanzados podemos definir una clase que marque una interfaz común.

```python
from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def tipo(self):
        pass
```

Subclase:

```python
class Alumno(Persona):
    def tipo(self):
        return "Alumno"
```

No es necesario utilizar clases abstractas en todos los proyectos, pero conviene conocer el concepto.

# Dataclasses

## 12. `@dataclass`

Cuando una clase se utiliza principalmente para almacenar datos, Python puede generar automáticamente métodos comunes.

```python
from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float
```

Uso:

```python
producto = Producto("Teclado", 25.0)
print(producto)
```

`dataclass` genera automáticamente, entre otros, `__init__` y una representación útil.

## 13. Composición con varias entidades

Ejemplo de biblioteca:

```text
Biblioteca
 ├── libros: list[Libro]
 ├── usuarios: list[Usuario]
 └── prestamos: list[Prestamo]
```

`Prestamo` puede contener referencias a:

```text
Usuario
Libro
```

Esto permite representar relaciones reales entre entidades.

## 14. Diseño antes de programar

Antes de crear clases conviene responder:

1. ¿Qué entidades existen?
2. ¿Qué información pertenece a cada entidad?
3. ¿Qué comportamiento corresponde a cada entidad?
4. ¿Qué relaciones existen entre ellas?
5. ¿Existe una relación "es un"?
6. ¿Existe una relación "tiene un"?

## 15. Actividad

Diseña las clases necesarias para representar una biblioteca con:

- Libros.
- Usuarios.
- Préstamos.

Antes de programar, escribe para cada clase:

- Atributos.
- Métodos.
- Relaciones.

Después implementa las clases y crea un pequeño ejemplo que registre un préstamo.

---

[Anterior: 14. Programación orientada a objetos: fundamentos](14-poo-fundamentos.md) · [Índice](README.md) · [Siguiente: 16. Proyecto final integrador](16-proyecto-final.md)
