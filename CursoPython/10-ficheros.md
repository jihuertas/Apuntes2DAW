# 10. Trabajo con ficheros

## Objetivos

Aprender a hacer persistente la información de nuestros programas utilizando archivos de texto y a trabajar correctamente con rutas.

## 1. Persistencia

Hasta ahora los datos almacenados en variables desaparecen cuando el programa finaliza.

```python
alumnos = []
```

Si cerramos el programa, la lista desaparece.

Los ficheros permiten guardar datos en almacenamiento permanente.

## 2. Abrir un fichero

Forma básica:

```python
fichero = open("datos.txt", "r", encoding="utf-8")
```

Al finalizar deberíamos cerrarlo:

```python
fichero.close()
```

## 3. Utilizar `with`

La forma recomendada es:

```python
with open("datos.txt", "r", encoding="utf-8") as fichero:
    contenido = fichero.read()
```

Cuando termina el bloque, Python cierra automáticamente el archivo.

## 4. Modos de apertura

| Modo | Uso |
|---|---|
| `r` | lectura |
| `w` | escritura, reemplazando el contenido |
| `a` | añadir al final |
| `x` | crear; falla si ya existe |
| `b` | modo binario |

Ejemplo:

```python
with open("datos.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Hola")
```

**Atención:** `w` elimina el contenido anterior.

## 5. Leer todo el contenido

```python
with open("datos.txt", encoding="utf-8") as fichero:
    contenido = fichero.read()

print(contenido)
```

## 6. Leer una línea

```python
with open("datos.txt", encoding="utf-8") as fichero:
    linea = fichero.readline()
```

## 7. Leer todas las líneas

```python
with open("datos.txt", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
```

`lineas` será una lista.

## 8. Recorrer línea a línea

Normalmente es preferible:

```python
with open("datos.txt", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea)
```

Esto evita cargar el archivo completo cuando no es necesario.

## 9. Saltos de línea

Una línea suele incluir `\n` al final.

```python
for linea in fichero:
    print(linea.strip())
```

`strip()` elimina espacios y saltos alrededor del texto.

## 10. Escribir

```python
with open("datos.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Ana\n")
    fichero.write("Luis\n")
```

## 11. Añadir

```python
with open("datos.txt", "a", encoding="utf-8") as fichero:
    fichero.write("Marta\n")
```

No se borra el contenido existente.

## 12. `writelines()`

```python
alumnos = ["Ana\n", "Luis\n", "Marta\n"]

with open("datos.txt", "w", encoding="utf-8") as fichero:
    fichero.writelines(alumnos)
```

`writelines()` no añade automáticamente saltos de línea.

## 13. Codificación

Conviene especificar:

```python
encoding="utf-8"
```

Especialmente cuando manejamos tildes, `ñ` u otros caracteres no ASCII.

## 14. Rutas relativas

```python
open("datos/alumnos.txt")
```

La ruta se interpreta respecto al directorio de trabajo actual, no necesariamente respecto al archivo `.py`.

Esto puede provocar confusión en proyectos grandes.

## 15. `pathlib`

Python dispone de una API moderna para trabajar con rutas.

```python
from pathlib import Path

ruta = Path("datos") / "alumnos.txt"
```

Comprobar existencia:

```python
if ruta.exists():
    print("El fichero existe")
```

Crear directorios:

```python
carpeta = Path("datos")
carpeta.mkdir(exist_ok=True)
```

## 16. Ruta basada en el archivo actual

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos" / "alumnos.txt"
```

Esto hace que la ruta sea independiente del directorio desde el que se ejecute el programa.

## 17. Métodos de `Path`

```python
ruta.exists()
ruta.is_file()
ruta.is_dir()
ruta.name
ruta.stem
ruta.suffix
ruta.parent
```

## 18. Leer y escribir con `Path`

```python
ruta = Path("mensaje.txt")
ruta.write_text("Hola", encoding="utf-8")
contenido = ruta.read_text(encoding="utf-8")
```

Para casos simples puede resultar muy cómodo.

## 19. Ejemplo: registro de eventos

```python
from datetime import datetime


def registrar_evento(mensaje):
    with open("registro.log", "a", encoding="utf-8") as fichero:
        ahora = datetime.now().isoformat(timespec="seconds")
        fichero.write(f"{ahora} - {mensaje}\n")
```

## 20. Actividad principal

Crea un pequeño gestor de tareas que almacene cada tarea en un fichero `tareas.txt`.

Menú:

```text
1. Añadir tarea
2. Mostrar tareas
3. Vaciar tareas
0. Salir
```

Después crea una segunda versión utilizando `pathlib`.

---

[Anterior: 09. *args, **kwargs, lambda y decoradores](09-funciones-avanzadas.md) · [Índice](README.md) · [Siguiente: 11. JSON y CSV](11-json-csv.md)
