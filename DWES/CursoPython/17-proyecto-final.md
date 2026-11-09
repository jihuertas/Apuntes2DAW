# 17. Proyecto final: Sistema de gestión de biblioteca

En este proyecto vas a desarrollar una aplicación completa en **Python** que integre los principales contenidos trabajados durante el curso.

El objetivo no es únicamente conseguir que el programa funcione. Tendrás que analizar el problema, diseñar una solución adecuada, organizar correctamente el código y aplicar los conceptos aprendidos.

> En este proyecto no se proporciona la estructura de clases ni los métodos que debes implementar. Parte del trabajo consiste precisamente en **diseñar la solución**.

---

## 1. Descripción del proyecto

Una biblioteca necesita una aplicación que permita gestionar:

- Los libros disponibles.
- Los usuarios registrados.
- Los préstamos de libros.
- Las devoluciones.
- La información almacenada entre distintas ejecuciones del programa.

La aplicación funcionará inicialmente mediante un **menú de consola**.

Un posible ejemplo de ejecución sería:

```text
=================================
      GESTIÓN DE BIBLIOTECA
=================================

1. Registrar libro
2. Registrar usuario
3. Buscar libro
4. Listar libros
5. Realizar préstamo
6. Registrar devolución
7. Mostrar préstamos activos
8. Mostrar préstamos de un usuario
9. Guardar datos
0. Salir

Selecciona una opción:
```

Este menú es únicamente orientativo. Puedes modificarlo o ampliarlo si lo consideras necesario.

---

# 2. Requisitos generales

La aplicación deberá estar desarrollada utilizando los contenidos estudiados durante el curso.

Será obligatorio utilizar:

- Variables y estructuras de control.
- Listas y diccionarios.
- Funciones.
- Programación orientada a objetos.
- Varias clases relacionadas entre sí.
- Módulos y paquetes.
- Lectura y escritura de ficheros.
- Formato JSON para la persistencia de datos.
- Gestión de excepciones.
- Un programa principal desde el que se ejecute la aplicación.

El código deberá estar correctamente organizado y evitar, en la medida de lo posible, la repetición de código.

---

# 3. Gestión de libros

La aplicación deberá permitir registrar los libros de la biblioteca.

De cada libro será necesario almacenar, como mínimo:

- Un identificador único.
- Título.
- Autor.
- Año de publicación.
- Género.
- Estado de disponibilidad.

Ejemplo de información:

```text
Código: L001
Título: El nombre de la rosa
Autor: Umberto Eco
Año: 1980
Género: Novela
Disponible: Sí
```

El programa deberá permitir:

- Registrar nuevos libros.
- Mostrar todos los libros.
- Buscar un libro por su identificador.
- Buscar libros por título.
- Buscar libros por autor.
- Consultar si un libro está disponible.

No podrán existir dos libros con el mismo identificador.

---

# 4. Gestión de usuarios

La biblioteca también deberá mantener un registro de sus usuarios.

De cada usuario se almacenará, como mínimo:

- Identificador.
- Nombre.
- Apellidos.
- Correo electrónico.

Por ejemplo:

```text
Identificador: U001
Nombre: Ana
Apellidos: García López
Email: ana@email.com
```

La aplicación deberá permitir:

- Registrar usuarios.
- Buscar un usuario.
- Mostrar todos los usuarios.

No podrán existir dos usuarios con el mismo identificador.

---

# 5. Gestión de préstamos

La aplicación deberá permitir que un usuario registrado pueda tomar prestado un libro.

Para realizar un préstamo será necesario conocer:

- El usuario.
- El libro.
- La fecha del préstamo.

El sistema deberá comprobar que la operación es válida antes de realizarla.

Por ejemplo:

```text
Usuario: U001
Libro: L003

Préstamo realizado correctamente.
```

Una vez realizado el préstamo, el libro deberá aparecer como **no disponible**.

---

# 6. Devoluciones

El sistema deberá permitir registrar la devolución de un libro.

Al realizar una devolución:

1. Se deberá localizar el préstamo correspondiente.
2. Se registrará la devolución.
3. El libro volverá a estar disponible.

Ejemplo:

```text
Código del libro: L003

Libro devuelto correctamente.
```

---

# 7. Reglas de negocio

La aplicación deberá controlar, como mínimo, las siguientes situaciones:

### Libros

- No puede haber dos libros con el mismo identificador.
- No puede prestarse un libro que ya esté prestado.
- No puede devolverse un libro que no tenga un préstamo activo.

### Usuarios

- No puede haber dos usuarios con el mismo identificador.
- No puede realizarse un préstamo a un usuario inexistente.

### Préstamos

- El libro debe existir.
- El usuario debe existir.
- El libro debe estar disponible.
- Una devolución solamente podrá realizarse sobre un préstamo activo.

El programa deberá informar claramente al usuario cuando una operación no pueda realizarse.

Por ejemplo:

```text
ERROR: El libro L003 ya se encuentra prestado.
```

---

# 8. Consultas

Además de las operaciones anteriores, la aplicación deberá permitir realizar diferentes consultas.

Como mínimo:

- Mostrar todos los libros.
- Mostrar únicamente los libros disponibles.
- Mostrar los libros prestados.
- Buscar libros por título.
- Buscar libros por autor.
- Mostrar todos los usuarios.
- Mostrar los préstamos activos.
- Mostrar los préstamos realizados por un usuario determinado.

Ejemplo:

```text
PRÉSTAMOS DE ANA GARCÍA

L001 - 1984
L008 - El nombre de la rosa
```

---

# 9. Persistencia de datos

Una característica fundamental de la aplicación será que los datos **no desaparezcan al cerrar el programa**.

Para ello deberás utilizar ficheros en formato **JSON**.

Como mínimo será necesario conservar:

- Libros.
- Usuarios.
- Préstamos.

Al iniciar la aplicación se deberán recuperar los datos almacenados anteriormente.

Al finalizar el programa se deberán guardar los cambios realizados.

Puedes decidir si utilizas:

```text
libros.json
usuarios.json
prestamos.json
```

o si prefieres almacenar toda la información en un único fichero.

La elección forma parte del diseño de la aplicación.

---

# 10. Gestión de errores

La aplicación deberá controlar posibles errores durante su ejecución.

Por ejemplo:

- Ficheros que todavía no existen.
- Datos introducidos con un formato incorrecto.
- Identificadores inexistentes.
- Intentos de registrar elementos duplicados.
- Operaciones de préstamo no permitidas.
- Operaciones de devolución no permitidas.

Deberás utilizar adecuadamente:

```python
try
except
```

cuando sea necesario.

El programa no debería finalizar inesperadamente ante un error que pueda ser controlado.

---

# 11. Diseño orientado a objetos

La aplicación deberá estar desarrollada utilizando **Programación Orientada a Objetos**.

Antes de comenzar a programar deberás analizar el problema y decidir:

- Qué clases son necesarias.
- Qué responsabilidad tendrá cada clase.
- Qué atributos necesita cada una.
- Qué métodos debe proporcionar.
- Cómo se relacionarán los diferentes objetos.

> No empieces directamente a escribir código. Primero diseña la estructura de la aplicación.

Como parte de la documentación del proyecto deberás explicar brevemente las clases que has creado y la responsabilidad de cada una.

---

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

---

# 13. Programa principal

El programa principal deberá mostrar un menú que permita acceder a las diferentes funcionalidades.

Por ejemplo:

```text
=================================
      GESTIÓN DE BIBLIOTECA
=================================

1. Registrar libro
2. Registrar usuario
3. Buscar libro
4. Listar libros
5. Realizar préstamo
6. Registrar devolución
7. Mostrar préstamos activos
8. Mostrar préstamos de un usuario
9. Guardar datos
0. Salir

Selecciona una opción:
```

El menú deberá permanecer activo hasta que el usuario seleccione la opción de salir.

---

# 14. Validación de datos

Los datos introducidos por el usuario deberán validarse.

Por ejemplo:

- Un año deberá ser un número válido.
- Un identificador no podrá estar vacío.
- Un libro no podrá registrarse dos veces.
- Un usuario no podrá registrarse dos veces.
- No se podrá seleccionar una opción inexistente del menú.

Cuando se produzca un error, el programa deberá informar al usuario y permitirle volver a intentarlo.

---

# 15. Desarrollo del proyecto

Se recomienda desarrollar el proyecto de forma progresiva.

### Fase 1. Análisis

Antes de programar:

1. Identifica los elementos principales del sistema.
2. Decide qué clases necesitarás.
3. Define sus atributos.
4. Define sus métodos.
5. Decide cómo se relacionarán.

---

### Fase 2. Modelo de datos

Implementa las clases principales.

Comprueba que puedes crear objetos correctamente antes de continuar.

---

### Fase 3. Gestión

Implementa las operaciones principales:

- Registrar.
- Buscar.
- Listar.
- Modificar estados.
- Realizar préstamos.
- Realizar devoluciones.

Prueba cada funcionalidad de forma independiente.

---

### Fase 4. Persistencia

Implementa la lectura y escritura de los ficheros JSON.

Comprueba que puedes:

1. Ejecutar el programa.
2. Registrar información.
3. Cerrar el programa.
4. Volver a ejecutarlo.
5. Recuperar la información anterior.

---

### Fase 5. Interfaz de consola

Implementa el menú principal y conecta todas las funcionalidades.

---

### Fase 6. Validación y excepciones

Prueba situaciones incorrectas:

```text
Prestar un libro inexistente.
Prestar un libro ya prestado.
Devolver un libro disponible.
Registrar un usuario duplicado.
Introducir una opción incorrecta.
```

La aplicación deberá controlar correctamente estas situaciones.

---

### Fase 7. Pruebas finales

Antes de entregar, comprueba todas las funcionalidades.

No pruebes únicamente los casos en los que todo funciona correctamente.

---

# 16. Documentación

El proyecto deberá incluir un fichero:

```text
README.md
```

que explique como mínimo:

## Descripción

Qué problema resuelve la aplicación.

## Instalación

Cómo obtener y preparar el proyecto.

## Ejecución

Cómo iniciar la aplicación.

Por ejemplo:

```bash
python main.py
```

## Estructura

Explicación de la organización de carpetas y módulos.

## Diseño

Explicación breve de las clases desarrolladas y de sus responsabilidades.

## Funcionalidades

Listado de las principales funcionalidades disponibles.

---

# 17. Repositorio Git

El proyecto deberá desarrollarse utilizando **Git** y almacenarse en un repositorio.

El repositorio deberá contener:

```text
README.md
.gitignore
```

y todos los ficheros necesarios para ejecutar la aplicación.

Si el proyecto utiliza alguna biblioteca externa, deberá incluir también:

```text
requirements.txt
```

El repositorio **no deberá contener**:

- Entornos virtuales.
- Ficheros temporales.
- Configuraciones del IDE.
- Ficheros generados automáticamente que no sean necesarios.

---

# 18. Requisitos mínimos para considerar el proyecto completado

Para considerar el proyecto terminado deberán funcionar correctamente, como mínimo:

- [ ] Registro de libros.
- [ ] Registro de usuarios.
- [ ] Búsqueda de libros.
- [ ] Listado de libros.
- [ ] Préstamo de libros.
- [ ] Devolución de libros.
- [ ] Control de disponibilidad.
- [ ] Consulta de préstamos activos.
- [ ] Consulta de préstamos de un usuario.
- [ ] Persistencia utilizando JSON.
- [ ] Recuperación de los datos al iniciar.
- [ ] Gestión de errores.
- [ ] Uso de Programación Orientada a Objetos.
- [ ] Organización mediante módulos y paquetes.
- [ ] Menú de consola.
- [ ] Repositorio Git correctamente organizado.
- [ ] Documentación mediante `README.md`.

---

# 19. Ampliaciones opcionales

Una vez completados todos los requisitos anteriores puedes añadir nuevas funcionalidades.

Algunas posibilidades son:

### Límite de préstamos

Establecer un número máximo de libros que puede tener prestados simultáneamente un usuario.

### Fecha límite

Registrar una fecha máxima de devolución.

### Préstamos atrasados

Mostrar los préstamos cuya fecha de devolución haya vencido.

### Historial

Mantener un historial de todos los préstamos realizados, incluyendo los ya devueltos.

### Estadísticas

Mostrar información como:

- Libro más prestado.
- Usuario que más libros ha solicitado.
- Número de préstamos realizados.
- Número de libros disponibles.
- Número de libros prestados.

### Eliminación y modificación

Permitir modificar o eliminar libros y usuarios controlando que la operación sea posible.

### Exportación

Permitir exportar determinados datos a CSV.

---

# 20. Objetivo final

Al finalizar el proyecto deberás haber construido una aplicación completa aplicando de forma conjunta los principales contenidos estudiados en Python:

```text
Estructuras de control
        ↓
Listas y diccionarios
        ↓
Funciones
        ↓
Programación Orientada a Objetos
        ↓
Módulos y paquetes
        ↓
Ficheros y JSON
        ↓
Excepciones
        ↓
Aplicación completa
```

El objetivo del proyecto no es únicamente obtener un programa que funcione.

También se valorará que seas capaz de:

- Analizar un problema.
- Diseñar una solución.
- Dividir el problema en partes.
- Elegir las estructuras de datos adecuadas.
- Diseñar correctamente las clases.
- Organizar el código.
- Evitar código repetido.
- Controlar situaciones de error.
- Documentar el proyecto.

> **Recuerda:** en un proyecto real normalmente conocemos los requisitos que debe cumplir la aplicación, pero no recibimos el código ni la estructura exacta que debemos utilizar. Diseñar esa solución también forma parte del trabajo de un desarrollador.
