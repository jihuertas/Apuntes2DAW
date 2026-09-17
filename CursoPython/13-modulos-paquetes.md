# 13. Módulos y paquetes

## Objetivos

Aprender a dividir aplicaciones grandes en varios archivos y carpetas manteniendo una estructura clara y reutilizable.

## 1. Problema de un único archivo

Al principio un programa puede caber en `main.py`, pero pronto aparecen cientos de líneas con responsabilidades distintas.

```text
main.py
```

Puede terminar conteniendo:

- Menús.
- Lectura de archivos.
- Validaciones.
- Operaciones con alumnado.
- Configuración.

Dividir el código mejora su mantenimiento.

## 2. ¿Qué es un módulo?

En términos prácticos, un archivo `.py` que puede importarse desde otro archivo.

Archivo `operaciones.py`:

```python
def sumar(a, b):
    return a + b
```

Archivo `main.py`:

```python
import operaciones

resultado = operaciones.sumar(5, 3)
print(resultado)
```

## 3. `from ... import ...`

```python
from operaciones import sumar

print(sumar(5, 3))
```

## 4. Alias

```python
import operaciones as op

print(op.sumar(5, 3))
```

Con bibliotecas es frecuente encontrar convenciones como alias breves, siempre que sean conocidas y mejoren la lectura.

## 5. Evitar `import *`

```python
from operaciones import *
```

No suele recomendarse porque dificulta saber de dónde procede cada nombre y puede provocar colisiones.

## 6. Biblioteca estándar

Python incluye numerosos módulos:

```python
import math
import random
import json
from pathlib import Path
from datetime import datetime
```

Ejemplo:

```python
import math

print(math.sqrt(25))
```

## 7. `__name__`

Cada módulo posee una variable especial `__name__`.

Si ejecutamos directamente:

```bash
python main.py
```

entonces en ese archivo:

```python
__name__ == "__main__"
```

Por eso es habitual:

```python
def main():
    print("Aplicación iniciada")


if __name__ == "__main__":
    main()
```

Si otro módulo importa este archivo, `main()` no se ejecutará automáticamente.

## 8. Ejemplo de separación

Antes:

```text
main.py
```

Después:

```text
proyecto/
├── main.py
├── alumnos.py
└── ficheros.py
```

`alumnos.py`:

```python
def buscar_alumno(alumnos, nombre):
    for alumno in alumnos:
        if alumno["nombre"].lower() == nombre.lower():
            return alumno
    return None
```

`ficheros.py`:

```python
import json


def guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as fichero:
        json.dump(datos, fichero, ensure_ascii=False, indent=4)
```

`main.py`:

```python
from alumnos import buscar_alumno
from ficheros import guardar_json
```

## 9. ¿Qué es un paquete?

Un paquete agrupa módulos dentro de un directorio.

```text
proyecto/
├── main.py
├── modelos/
│   ├── alumno.py
│   └── profesor.py
└── utilidades/
    ├── validaciones.py
    └── ficheros.py
```

Importación:

```python
from utilidades.ficheros import guardar_json
```

## 10. `__init__.py`

Tradicionalmente los paquetes incluyen:

```text
__init__.py
```

Python moderno admite ciertos paquetes sin él, pero continúa siendo útil para definir claramente paquetes y controlar exportaciones.

```text
modelos/
├── __init__.py
├── alumno.py
└── profesor.py
```

## 11. Importaciones absolutas

```python
from modelos.alumno import Alumno
```

Suelen ser fáciles de entender porque muestran claramente la ruta dentro del proyecto.

## 12. Importaciones relativas

Dentro de un paquete también existen formas como:

```python
from .alumno import Alumno
```

Conviene utilizarlas entendiendo bien la estructura del paquete.

## 13. Separación por responsabilidades

Una estructura razonable:

```text
gestor_alumnos/
├── main.py
├── modelos/
├── servicios/
├── utilidades/
└── datos/
```

No es necesario crear carpetas sin necesidad. La estructura debe crecer con el proyecto.

## 14. `requirements.txt`

Los módulos propios no se instalan con `pip`, pero las dependencias externas sí.

```bash
pip freeze > requirements.txt
```

El repositorio debería incluir `requirements.txt`, no el entorno `.venv`.

## 15. Actividad principal

Refactoriza la aplicación de alumnado con esta estructura:

```text
gestor_alumnos/
├── main.py
├── alumnos.py
├── ficheros.py
├── validaciones.py
├── datos/
│   └── alumnos.json
└── README.md
```

Requisitos:

- `main.py` contiene el menú y coordina el programa.
- `alumnos.py` contiene operaciones relacionadas con alumnado.
- `ficheros.py` contiene lectura y escritura JSON.
- `validaciones.py` contiene funciones reutilizables para validar entrada.
- Ningún módulo debería ejecutar el programa principal al ser importado.

---

[Anterior: 12. Excepciones](12-excepciones.md) · [Índice](README.md) · [Siguiente: 14. Programación orientada a objetos: fundamentos](14-poo-fundamentos.md)
