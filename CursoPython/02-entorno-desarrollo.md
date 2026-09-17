# 02. Entorno de desarrollo

## Objetivos

En este tema prepararemos el entorno con el que desarrollaremos nuestros programas y aprenderemos a distinguir Python, el intérprete, el editor de código, la terminal, `pip` y los entornos virtuales.

## 1. Comprobar la instalación de Python

En una terminal:

```bash
python --version
```

En determinados sistemas:

```bash
python3 --version
```

El resultado será similar a:

```text
Python 3.x.x
```

Durante el curso utilizaremos Python 3.

## 2. Intérprete interactivo

Podemos iniciar Python directamente desde la terminal:

```bash
python
```

Aparecerá el prompt:

```text
>>>
```

Ahora podemos ejecutar instrucciones inmediatamente:

```python
>>> 2 + 3
5
>>> print("Hola")
Hola
```

El intérprete interactivo resulta especialmente útil para probar pequeñas expresiones.

Para salir:

```python
exit()
```

## 3. Scripts `.py`

Los programas normales se almacenan en archivos de texto con extensión `.py`.

Archivo `hola.py`:

```python
print("Hola mundo")
```

Ejecución:

```bash
python hola.py
```

## 4. Directorio de trabajo

Cuando ejecutamos un programa, es importante conocer desde qué carpeta estamos trabajando.

Ejemplo:

```text
curso-python/
├── README.md
└── ejemplos/
    └── hola.py
```

Podemos acceder desde terminal:

```bash
cd curso-python/ejemplos
python hola.py
```

## 5. Editor e IDE

Un editor facilita la escritura del código. Un IDE añade herramientas como depuración, gestión de proyectos, autocompletado o integración con sistemas de control de versiones.

Opciones habituales:

- Visual Studio Code.
- PyCharm.
- Sublime Text.
- Vim/Neovim.

Durante el curso puede utilizarse Visual Studio Code.

## 6. Visual Studio Code

Elementos importantes:

- Explorador de archivos.
- Editor.
- Terminal integrada.
- Sistema de extensiones.
- Depurador.
- Control de versiones.

Para trabajar con Python conviene instalar la extensión oficial de Python de Microsoft.

## 7. Seleccionar el intérprete

Un equipo puede tener varios intérpretes de Python. Visual Studio Code necesita saber cuál debe utilizar.

En la paleta de comandos:

```text
Python: Select Interpreter
```

Más adelante seleccionaremos el intérprete perteneciente al entorno virtual del proyecto.

## 8. Terminal integrada

En Visual Studio Code:

```text
Terminal → New Terminal
```

Desde ella podemos ejecutar:

```bash
python programa.py
```

Esto permite trabajar sin abandonar el editor.

## 9. `pip`: gestor de paquetes

Python incluye una biblioteca estándar amplia, pero no todas las funcionalidades posibles vienen instaladas.

Con `pip` podemos instalar paquetes externos.

```bash
pip install requests
```

Consultar paquetes instalados:

```bash
pip list
```

Consultar información de uno:

```bash
pip show requests
```

Desinstalar:

```bash
pip uninstall requests
```

En algunos sistemas resulta recomendable utilizar:

```bash
python -m pip install requests
```

Así nos aseguramos de ejecutar el `pip` asociado al intérprete seleccionado.

## 10. ¿Por qué utilizar entornos virtuales?

Supongamos que tenemos dos proyectos:

```text
Proyecto A → necesita una determinada versión de una librería
Proyecto B → necesita otra versión
```

Si instalamos todo globalmente pueden aparecer conflictos.

Un entorno virtual crea un entorno Python aislado para cada proyecto.

## 11. Crear un entorno virtual

Dentro de la carpeta del proyecto:

```bash
python -m venv .venv
```

Estructura:

```text
mi-proyecto/
├── .venv/
└── main.py
```

`.venv` es un nombre habitual, aunque podría utilizarse otro.

## 12. Activar el entorno

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

Al activarlo suele aparecer:

```text
(.venv)
```

## 13. Instalar dependencias dentro del entorno

Con el entorno activo:

```bash
python -m pip install requests
```

La librería quedará instalada únicamente en ese entorno.

## 14. Desactivar

```bash
deactivate
```

## 15. `requirements.txt`

Podemos guardar las dependencias actuales:

```bash
pip freeze > requirements.txt
```

Ejemplo:

```text
requests==2.x.x
```

Otra persona puede reproducir el entorno mediante:

```bash
pip install -r requirements.txt
```

## 16. `.gitignore`

Normalmente no se sube `.venv` al repositorio Git.

Archivo `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
```

Sí deberíamos versionar `requirements.txt`.

## 17. Depuración básica

Un depurador permite ejecutar el programa paso a paso y observar los valores de las variables.

Conceptos básicos:

- Breakpoint o punto de interrupción.
- Step over.
- Step into.
- Continue.
- Variables.
- Call stack.

No es necesario dominar todavía todas estas herramientas, pero conviene acostumbrarse a no depurar únicamente añadiendo `print()`.

## 18. Estructura recomendada para las prácticas

```text
practica-01/
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

## Actividad

1. Crea una carpeta `mi-primer-proyecto`.
2. Crea un entorno virtual `.venv`.
3. Actívalo.
4. Crea `main.py`.
5. Instala `requests`.
6. Genera `requirements.txt`.
7. Añade `.venv/` a `.gitignore`.
8. Ejecuta `main.py` desde la terminal integrada.

---

[Anterior: 01. Introducción a Python](01-introduccion.md) · [Índice](README.md) · [Siguiente: 03. Variables, constantes y tipos de datos](03-variables-constantes-tipos.md)
