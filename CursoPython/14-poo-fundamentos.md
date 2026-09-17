# 14. Programación orientada a objetos: fundamentos

## Objetivos

Comprender los conceptos de clase, objeto, atributo y método y aprender a modelar entidades del mundo real mediante Python.

## 1. Del diccionario al objeto

Hasta ahora podemos representar un alumno así:

```python
alumno = {
    "nombre": "Ana",
    "edad": 18,
    "notas": [7, 8, 9],
}
```

Es válido, pero el comportamiento queda separado de los datos.

Por ejemplo:

```python
def calcular_media(alumno):
    return sum(alumno["notas"]) / len(alumno["notas"])
```

La programación orientada a objetos propone agrupar datos y comportamiento relacionados.

## 2. Clase y objeto

Una **clase** describe cómo serán determinados objetos.

```python
class Alumno:
    pass
```

Crear una instancia:

```python
ana = Alumno()
```

- `Alumno` es la clase.
- `ana` es un objeto o instancia.

## 3. Constructor `__init__`

```python
class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Crear objetos:

```python
ana = Alumno("Ana", 18)
luis = Alumno("Luis", 19)
```

Cada objeto conserva sus propios valores.

## 4. `self`

`self` representa la instancia actual.

```python
self.nombre = nombre
```

El `nombre` de la derecha es el parámetro recibido; `self.nombre` es el atributo almacenado en el objeto.

## 5. Atributos

```python
print(ana.nombre)
print(ana.edad)
```

Podemos modificarlos:

```python
ana.edad = 19
```

## 6. Métodos

Un método es una función definida dentro de una clase y asociada a sus objetos.

```python
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def añadir_nota(self, nota):
        self.notas.append(nota)
```

Uso:

```python
ana = Alumno("Ana")
ana.añadir_nota(8)
ana.añadir_nota(9)
```

## 7. Métodos que devuelven valores

```python
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def calcular_media(self):
        if not self.notas:
            return None
        return sum(self.notas) / len(self.notas)
```

## 8. Validar desde el objeto

```python
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def añadir_nota(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        self.notas.append(nota)
```

Ahora el propio objeto protege sus reglas básicas.

## 9. Atributos de clase

```python
class Alumno:
    centro = "IES Ejemplo"

    def __init__(self, nombre):
        self.nombre = nombre
```

`centro` pertenece a la clase y se comparte conceptualmente entre instancias.

```python
print(Alumno.centro)
print(ana.centro)
```

## 10. Atributos de instancia

```python
self.nombre
self.edad
self.notas
```

Son específicos de cada objeto.

## 11. Encapsulación por convención

Python no utiliza el mismo modelo de privacidad estricta de otros lenguajes.

Un atributo con un guion bajo indica que se considera de uso interno:

```python
self._nota
```

No impide técnicamente acceder, pero comunica intención.

## 12. Propiedades

```python
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self._nota = nota

    @property
    def nota(self):
        return self._nota
```

Uso:

```python
print(ana.nota)
```

## 13. Setter

```python
@nota.setter
def nota(self, valor):
    if not 0 <= valor <= 10:
        raise ValueError("Nota fuera de rango")
    self._nota = valor
```

Entonces:

```python
ana.nota = 9
```

utiliza el setter.

## 14. `__str__`

Define una representación legible para el usuario.

```python
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
```

```python
print(ana)
```

## 15. `__repr__`

Suele ofrecer una representación útil para desarrollo y depuración.

```python
def __repr__(self):
    return f"Alumno(nombre={self.nombre!r})"
```

## 16. `__eq__`

Podemos definir cuándo dos objetos se consideran iguales.

```python
def __eq__(self, otro):
    if not isinstance(otro, Alumno):
        return NotImplemented
    return self.nombre == otro.nombre
```

## 17. Métodos de clase

```python
class Alumno:
    total = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Alumno.total += 1

    @classmethod
    def numero_alumnos(cls):
        return cls.total
```

## 18. Métodos estáticos

```python
class Alumno:
    @staticmethod
    def nota_valida(nota):
        return 0 <= nota <= 10
```

No dependen de una instancia ni de la clase, aunque conceptualmente están relacionados con ella.

## 19. Ejemplo completo

```python
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def añadir_nota(self, nota):
        if not self.nota_valida(nota):
            raise ValueError("Nota fuera de rango")
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return None
        return sum(self.notas) / len(self.notas)

    @staticmethod
    def nota_valida(nota):
        return 0 <= nota <= 10

    def __str__(self):
        return self.nombre
```

## 20. Actividad principal

Transforma la estructura basada en diccionarios de la aplicación anterior en objetos `Alumno`.

Cada alumno debe disponer de:

- Nombre.
- Lista de notas.
- Método para añadir una nota.
- Método para calcular media.
- Validación del rango de notas.
- Representación mediante `__str__`.

---

[Anterior: 13. Módulos y paquetes](13-modulos-paquetes.md) · [Índice](README.md) · [Siguiente: 15. Programación orientada a objetos: herencia y composición](15-poo-avanzada.md)
