# 17. Proyecto final integrador

## Objetivo

Construir una aplicación completa de consola aplicando de forma conjunta los contenidos del curso.

El proyecto propuesto será un **sistema de gestión de biblioteca**.

No se pretende construir un producto comercial, sino practicar:

- Diseño del programa.
- Colecciones.
- Funciones.
- Ficheros.
- JSON.
- Excepciones.
- Módulos y paquetes.
- Programación orientada a objetos.

## 1. Requisitos funcionales

La aplicación debe permitir:

1. Registrar libros.
2. Registrar usuarios.
3. Buscar libros.
4. Listar libros.
5. Realizar préstamos.
6. Registrar devoluciones.
7. Consultar préstamos activos.
8. Guardar datos.
9. Recuperar datos al iniciar.
10. Salir de forma controlada.

## 2. Menú principal

```text
========== BIBLIOTECA ==========
1. Registrar libro
2. Registrar usuario
3. Buscar libro
4. Listar libros
5. Realizar préstamo
6. Devolver libro
7. Mostrar préstamos activos
8. Guardar datos
0. Salir
================================
```

## 3. Entidades principales

### Libro

Atributos posibles:

- ISBN.
- Título.
- Autor.
- Año.
- Disponibilidad.

Métodos posibles:

- Marcar como prestado.
- Marcar como disponible.
- Representación textual.

### Usuario

Atributos:

- Identificador.
- Nombre.
- Correo electrónico.

### Préstamo

Atributos:

- Usuario.
- Libro.
- Fecha de préstamo.
- Fecha prevista de devolución.
- Fecha real de devolución.

### Biblioteca

Responsabilidades:

- Gestionar colecciones de libros, usuarios y préstamos.
- Buscar entidades.
- Registrar préstamos.
- Registrar devoluciones.
- Aplicar las reglas de negocio.

## 4. Posible modelo

```text
Biblioteca
│
├── libros ──────────> Libro
├── usuarios ────────> Usuario
└── prestamos ───────> Prestamo
                         │
                         ├── Usuario
                         └── Libro
```

## 5. Estructura recomendada

```text
biblioteca/
├── README.md
├── requirements.txt
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── libro.py
│   ├── usuario.py
│   └── prestamo.py
├── servicios/
│   ├── __init__.py
│   └── biblioteca.py
├── utilidades/
│   ├── __init__.py
│   ├── ficheros.py
│   └── validaciones.py
└── datos/
    ├── libros.json
    ├── usuarios.json
    └── prestamos.json
```

## 6. Clase `Libro`

Una posible versión inicial:

```python
class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            raise ValueError("El libro ya está prestado")
        self.disponible = False

    def devolver(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"
```

## 7. Clase `Usuario`

```python
class Usuario:
    def __init__(self, identificador, nombre, email):
        self.identificador = identificador
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"{self.nombre} <{self.email}>"
```

## 8. Clase `Prestamo`

```python
from datetime import date


class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

    @property
    def activo(self):
        return self.fecha_devolucion is None
```

## 9. Servicio `Biblioteca`

```python
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
```

Métodos a implementar:

```python
registrar_libro()
registrar_usuario()
buscar_libro()
buscar_usuario()
prestar_libro()
devolver_libro()
listar_libros()
listar_prestamos_activos()
```

## 10. Búsqueda de libro

Ejemplo:

```python
def buscar_libro(self, isbn):
    for libro in self.libros:
        if libro.isbn == isbn:
            return libro
    return None
```

Más adelante podría mejorarse utilizando un diccionario indexado por ISBN.

## 11. Reglas de negocio

El sistema debería impedir:

- Registrar dos libros con el mismo ISBN.
- Registrar dos usuarios con el mismo identificador.
- Prestar un libro que ya está prestado.
- Devolver un libro que no tiene préstamo activo.
- Prestar un libro a un usuario inexistente.

Estas situaciones deben gestionarse de forma clara.

## 12. Persistencia

Los datos deben sobrevivir entre ejecuciones.

Una estrategia sencilla es convertir los objetos a diccionarios antes de escribir JSON.

```python
def libro_a_dict(libro):
    return {
        "isbn": libro.isbn,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "disponible": libro.disponible,
    }
```

Después:

```python
json.dump(datos, fichero, ensure_ascii=False, indent=4)
```

Al cargar, debemos reconstruir los objetos.

## 13. Excepciones

La interfaz de usuario debe controlar errores previsibles:

```python
try:
    biblioteca.prestar_libro(usuario_id, isbn)
except ValueError as error:
    print(f"No se pudo realizar el préstamo: {error}")
```

La capa de lógica no debería limitarse a imprimir errores; debería comunicar el problema al código que la llama.

## 14. Función `main()`

```python
def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "0":
            break

        # Gestionar el resto de opciones


if __name__ == "__main__":
    main()
```

## 15. Desarrollo por fases

### Fase 1

Crear las clases y probarlas manualmente.

### Fase 2

Crear `Biblioteca` y sus operaciones.

### Fase 3

Crear el menú interactivo.

### Fase 4

Añadir persistencia JSON.

### Fase 5

Añadir validación y excepciones.

### Fase 6

Refactorizar módulos y paquetes.

### Fase 7

Añadir pruebas y documentación.

## 16. Posibles ampliaciones

Una vez terminada la versión básica:

- Buscar libros por título o autor.
- Ordenar resultados.
- Limitar número de préstamos por usuario.
- Añadir fecha máxima de devolución.
- Detectar préstamos atrasados.
- Exportar información a CSV.
- Incorporar tests con `pytest`.
- Sustituir JSON por SQLite.
- Crear una API con FastAPI o Django REST Framework.
- Crear una interfaz web con Django.

## 17. Entrega recomendada

El repositorio debería contener:

```text
README.md
código fuente
ficheros de datos de ejemplo
.gitignore
requirements.txt
```

El `README.md` del proyecto debería explicar:

- Objetivo.
- Instalación.
- Creación del entorno virtual.
- Ejecución.
- Estructura del proyecto.
- Funcionalidades implementadas.

## 18. Cierre del curso

Al completar el proyecto habremos recorrido una progresión completa:

```text
variables
    ↓
condicionales
    ↓
bucles
    ↓
colecciones
    ↓
funciones
    ↓
persistencia
    ↓
excepciones
    ↓
módulos
    ↓
objetos
    ↓
aplicación estructurada
```


---

[Anterior: 15. Programación orientada a objetos: herencia y composición](15-poo-avanzada.md) · [Índice](README.md) · [Siguiente: Volver al índice](README.md)
