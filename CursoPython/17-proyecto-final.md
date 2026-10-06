# 12. Organización del proyecto

No se permitirá desarrollar toda la aplicación en un único fichero Python.

El proyecto deberá estar dividido utilizando **módulos y paquetes**, separando las distintas responsabilidades de la aplicación.

La organización concreta del proyecto forma parte del ejercicio, aunque puedes utilizar la siguiente estructura como referencia.

## Estructura recomendada

```text
biblioteca/
│
├── main.py
│
├── modelos/
│   ├── __init__.py
│   ├── libro.py
│   ├── usuario.py
│   └── prestamo.py
│
├── servicios/
│   ├── __init__.py
│   └── biblioteca.py
│
├── datos/
│   ├── libros.json
│   ├── usuarios.json
│   └── prestamos.json
│
├── README.md
├── .gitignore
└── requirements.txt
```

> Esta estructura es una **recomendación**. Puedes utilizar otra organización siempre que esté justificada y mantenga una separación adecuada de responsabilidades.

---

## `main.py`

Será el punto de entrada de la aplicación.

Su función principal será:

- Mostrar el menú.
- Solicitar datos al usuario.
- Llamar a las funciones o métodos correspondientes.
- Mostrar los resultados.

El fichero `main.py` no debería contener toda la lógica de funcionamiento de la aplicación.

La aplicación deberá poder iniciarse mediante:

```bash
python main.py
```

---

## Paquete `modelos`

Contendrá las clases utilizadas para representar los elementos principales de la aplicación.

Por ejemplo:

```text
modelos/
├── __init__.py
├── libro.py
├── usuario.py
└── prestamo.py
```

Cada fichero debería contener la clase correspondiente.

Por ejemplo:

```text
libro.py      → información y comportamiento de un libro
usuario.py    → información y comportamiento de un usuario
prestamo.py   → información y comportamiento de un préstamo
```

Puedes crear otras clases si consideras que son necesarias.

---

## Paquete `servicios`

Contendrá la lógica principal de gestión de la aplicación.

Por ejemplo:

```text
servicios/
├── __init__.py
└── biblioteca.py
```

Desde aquí podrían realizarse operaciones relacionadas con:

- Gestión de libros.
- Gestión de usuarios.
- Préstamos.
- Devoluciones.
- Búsquedas.
- Consultas.

La forma concreta de implementar estas operaciones forma parte del diseño del proyecto.

---

## Carpeta `datos`

Contendrá los ficheros utilizados para almacenar permanentemente la información.

Por ejemplo:

```text
datos/
├── libros.json
├── usuarios.json
└── prestamos.json
```

También puedes optar por utilizar un único fichero:

```text
datos/
└── biblioteca.json
```

La elección deberá ser coherente con el diseño de tu aplicación.

---

## `README.md`

Deberá contener la documentación básica del proyecto:

- Descripción.
- Instalación.
- Ejecución.
- Estructura del proyecto.
- Clases utilizadas.
- Funcionalidades disponibles.

---

## `.gitignore`

Deberá evitar que se añadan al repositorio archivos innecesarios.

Por ejemplo:

```gitignore
__pycache__/
*.pyc
.venv/
venv/
.idea/
.vscode/
```

---

## `requirements.txt`

Solamente será necesario si utilizas bibliotecas externas.

En ese caso deberá contener las dependencias necesarias para ejecutar el proyecto.

Por ejemplo:

```text
nombre_paquete==1.0.0
```

Si el proyecto utiliza exclusivamente módulos incluidos en Python, este fichero puede estar vacío o no ser necesario.

---

## Separación de responsabilidades

Una correcta organización del proyecto implica evitar situaciones como:

```python
# main.py

# Clase Libro
# Clase Usuario
# Clase Prestamo
# Lectura del JSON
# Escritura del JSON
# Gestión de préstamos
# Gestión de usuarios
# Menú
# ...
```

Todo el programa **no debe estar desarrollado dentro de `main.py`**.

En su lugar, cada parte de la aplicación deberá tener una responsabilidad concreta:

```text
modelos       → representan los datos
servicios     → gestionan la lógica de la aplicación
datos         → almacenan la información
main.py       → inicia la aplicación y gestiona la interacción con el usuario
```

El objetivo es conseguir una aplicación **modular, organizada y fácil de mantener**.
