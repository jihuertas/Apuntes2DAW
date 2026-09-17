# 11. JSON y CSV

## Objetivos

Aprender a almacenar datos estructurados en formatos muy utilizados para intercambiar información entre aplicaciones.

# JSON

## 1. ¿Qué es JSON?

JSON significa **JavaScript Object Notation** y es un formato de texto para representar datos estructurados.

Ejemplo:

```json
{
    "nombre": "Ana",
    "edad": 18,
    "activo": true
}
```

Es habitual encontrar JSON en:

- APIs.
- Ficheros de configuración.
- Intercambio de datos entre frontend y backend.
- Almacenamiento sencillo.

## 2. Relación con Python

Un objeto JSON se parece a un diccionario:

```python
alumno = {
    "nombre": "Ana",
    "edad": 18,
    "activo": True,
}
```

Equivalencias principales:

| Python | JSON |
|---|---|
| `dict` | object |
| `list` | array |
| `str` | string |
| `int`, `float` | number |
| `True` | true |
| `False` | false |
| `None` | null |

## 3. Módulo `json`

```python
import json
```

## 4. `json.dump()`

Guarda un objeto Python directamente en un fichero JSON.

```python
import json

alumno = {
    "nombre": "Ana",
    "edad": 18,
    "notas": [7, 8, 9],
}

with open("alumno.json", "w", encoding="utf-8") as fichero:
    json.dump(alumno, fichero, ensure_ascii=False, indent=4)
```

`ensure_ascii=False` permite conservar caracteres como `ñ` y tildes de forma legible.

`indent=4` produce un JSON formateado.

## 5. `json.load()`

```python
with open("alumno.json", encoding="utf-8") as fichero:
    alumno = json.load(fichero)

print(alumno["nombre"])
```

## 6. `dumps()` y `loads()`

`dumps()` trabaja con texto en lugar de fichero:

```python
texto_json = json.dumps(alumno, ensure_ascii=False)
```

`loads()` realiza la operación inversa:

```python
alumno = json.loads(texto_json)
```

Resumen:

```text
load   → fichero JSON a Python
dump   → Python a fichero JSON
loads  → texto JSON a Python
dumps  → Python a texto JSON
```

## 7. Guardar una colección

```python
alumnos = [
    {"nombre": "Ana", "notas": [7, 8]},
    {"nombre": "Luis", "notas": [5, 6]},
]

with open("alumnos.json", "w", encoding="utf-8") as fichero:
    json.dump(alumnos, fichero, ensure_ascii=False, indent=4)
```

## 8. Cargar al iniciar

```python
from pathlib import Path
import json

RUTA = Path("alumnos.json")


def cargar_alumnos():
    if not RUTA.exists():
        return []

    with RUTA.open(encoding="utf-8") as fichero:
        return json.load(fichero)
```

## 9. Guardar al finalizar

```python
def guardar_alumnos(alumnos):
    with RUTA.open("w", encoding="utf-8") as fichero:
        json.dump(alumnos, fichero, ensure_ascii=False, indent=4)
```

Esto permite que la aplicación de alumnado conserve sus datos entre ejecuciones.

# CSV

## 10. ¿Qué es CSV?

CSV representa datos tabulares mediante texto.

```csv
nombre,edad,nota
Ana,18,8.5
Luis,19,7.2
```

Es habitual para intercambiar información con hojas de cálculo y aplicaciones de gestión.

## 11. Módulo `csv`

```python
import csv
```

## 12. Leer con `csv.reader`

```python
with open("alumnos.csv", encoding="utf-8", newline="") as fichero:
    lector = csv.reader(fichero)

    for fila in lector:
        print(fila)
```

Cada fila se devuelve como una lista.

## 13. Leer con `DictReader`

Cuando la primera fila contiene encabezados:

```python
with open("alumnos.csv", encoding="utf-8", newline="") as fichero:
    lector = csv.DictReader(fichero)

    for alumno in lector:
        print(alumno["nombre"])
```

Cada fila se representa mediante un diccionario.

## 14. Escribir con `csv.writer`

```python
with open("alumnos.csv", "w", encoding="utf-8", newline="") as fichero:
    escritor = csv.writer(fichero)
    escritor.writerow(["nombre", "edad", "nota"])
    escritor.writerow(["Ana", 18, 8.5])
```

## 15. Escribir con `DictWriter`

```python
campos = ["nombre", "edad", "nota"]

with open("alumnos.csv", "w", encoding="utf-8", newline="") as fichero:
    escritor = csv.DictWriter(fichero, fieldnames=campos)
    escritor.writeheader()
    escritor.writerow({
        "nombre": "Ana",
        "edad": 18,
        "nota": 8.5,
    })
```

## 16. JSON o CSV

Utiliza CSV cuando:

- Los datos son tabulares.
- Todas las filas tienen una estructura similar.
- Se va a trabajar con una hoja de cálculo.

Utiliza JSON cuando:

- Existen estructuras anidadas.
- Hay listas dentro de objetos.
- Los datos proceden de una API.
- Necesitas una estructura más flexible.

## 17. Práctica principal

Modifica la aplicación de gestión de alumnado para que:

1. Lea `alumnos.json` al iniciar.
2. Si el fichero no existe, comience con una lista vacía.
3. Permita modificar los datos desde el menú.
4. Guarde los cambios en JSON antes de salir.
5. Incluya una opción para exportar un resumen a `alumnos.csv`.

---

[Anterior: 10. Trabajo con ficheros](10-ficheros.md) · [Índice](README.md) · [Siguiente: 12. Excepciones](12-excepciones.md)
