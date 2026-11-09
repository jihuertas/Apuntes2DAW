# Bloque 9. Configuración de Django con diferentes gestores de bases de datos

## Objetivos

- Identificar los principales gestores relacionales compatibles con Django.
- Comprender las opciones de conexión de `DATABASES`.
- Configurar el mismo proyecto con SQLite y PostgreSQL.
- Gestionar parámetros de configuración mediante variables de entorno y `config()`.
- Proteger las credenciales con un archivo `.env` excluido de Git.
- Aplicar migraciones en una base de datos nueva y reconocer sus implicaciones.

## 1. El ORM y la independencia del gestor

El ORM permite mantener buena parte del código de modelos y consultas al cambiar de gestor, aunque existen diferencias de tipos, funciones, restricciones y comportamiento transaccional.

| Gestor | Características | Uso habitual |
|---|---|---|
| SQLite | Base de datos en un archivo, sin servidor independiente | Aprendizaje y proyectos sencillos |
| PostgreSQL | Servidor relacional con amplias capacidades | Aplicaciones web y producción |
| MySQL | Servidor relacional ampliamente utilizado | Aplicaciones web |
| MariaDB | Alternativa compatible con el backend MySQL de Django | Aplicaciones web |

## 2. Configuración con SQLite

En `biblioteca/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

La base de datos se guarda en un archivo local. Es la configuración inicial habitual de un proyecto Django.

## 3. Configuración con PostgreSQL

Para esta práctica, se supone que PostgreSQL está instalado y funcionando, que existe una base de datos llamada `biblioteca` y un usuario con permisos sobre ella.

Instala el controlador en el entorno virtual:

```bash
python -m pip install "psycopg[binary]"
```

Una configuración directa en `settings.py` puede leer variables del sistema mediante `os.environ`:

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "biblioteca"),
        "USER": os.environ.get("DB_USER", "biblioteca_user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
```

En macOS/Linux se pueden establecer estas variables para una sesión de terminal:

```bash
export DB_NAME=biblioteca
export DB_USER=biblioteca_user
export DB_PASSWORD='tu_clave_local'
export DB_HOST=localhost
export DB_PORT=5432
python manage.py migrate
```

Sin embargo, escribir muchas variables en cada terminal resulta incómodo. En el siguiente apartado utilizaremos un archivo `.env` y la función `config()`.

## 4. Variables de entorno con `python-decouple` y `config()`

### 4.1. ¿Por qué separar la configuración del código?

Los datos de conexión, las claves y otras opciones pueden variar entre el ordenador de desarrollo y el servidor donde se despliega la aplicación. **No deben escribirse contraseñas reales directamente en `settings.py` ni publicarse en GitHub**.

La biblioteca `python-decouple` proporciona la función `config()`, que lee variables de entorno y también puede leerlas desde un archivo `.env`. Las variables del entorno del sistema tienen prioridad sobre las del archivo.

### 4.2. Instalar `python-decouple`

Desde el entorno virtual del proyecto:

```bash
python -m pip install python-decouple
```

En `biblioteca/settings.py`:

```python
from decouple import config
```

**Atención:** el paquete que se instala se llama `python-decouple`, pero el módulo que se importa es `decouple`.

### 4.3. Crear el archivo `.env`

Crea un archivo llamado `.env` en la raíz del proyecto, junto a `manage.py`:

```text
biblioteca/
├── manage.py
├── .env
├── .gitignore
├── biblioteca/
│   └── settings.py
└── catalogo/
```

Contenido de ejemplo para PostgreSQL (sustituye los valores por los de tu instalación local):

```dotenv
DB_ENGINE=postgresql
DB_NAME=biblioteca
DB_USER=biblioteca_user
DB_PASSWORD=tu_clave_local
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
```

Para utilizar SQLite, basta con cambiar:

```dotenv
DB_ENGINE=sqlite
DEBUG=True
```

El archivo `.env` no se sube al repositorio. Cada persona puede tener sus propios valores.

### 4.4. Leer parámetros con `config()`

La función `config()` recibe el nombre de la variable y, opcionalmente, un valor predeterminado y un tipo de conversión.

```python
from decouple import config

nombre_bd = config("DB_NAME", default="biblioteca")
puerto = config("DB_PORT", default=5432, cast=int)
modo_debug = config("DEBUG", default=False, cast=bool)
```

| Expresión | Resultado |
|---|---|
| `config("DB_NAME")` | Lee la variable; produce un error si no existe |
| `config("DB_NAME", default="biblioteca")` | Utiliza `biblioteca` si no está definida |
| `config("DB_PORT", default=5432, cast=int)` | Convierte el valor a entero |
| `config("DEBUG", default=False, cast=bool)` | Convierte valores como `True` o `False` a booleanos |

**Importante:** no utilices `bool(config("DEBUG"))`, porque una cadena no vacía como `"False"` se evaluaría como verdadera. Usa `cast=bool`.

### 4.5. Configurar SQLite y PostgreSQL desde el mismo `settings.py`

Sustituye la configuración anterior de `DATABASES` por la siguiente:

```python
from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)

DB_ENGINE = config("DB_ENGINE", default="sqlite").lower()

if DB_ENGINE == "sqlite":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
elif DB_ENGINE == "postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST", default="localhost"),
            "PORT": config("DB_PORT", default=5432, cast=int),
        }
    }
else:
    raise ValueError(f"Gestor de base de datos no admitido: {DB_ENGINE}")
```

Con esta configuración:

1. `DB_ENGINE=sqlite` utiliza el archivo `db.sqlite3`.
2. `DB_ENGINE=postgresql` utiliza los parámetros de conexión de PostgreSQL.
3. No es necesario editar `settings.py` para cambiar de gestor.
4. Si falta una credencial necesaria para PostgreSQL, `config()` avisará de que la variable no está definida.

> **Nota:** esta configuración es didáctica y permite cambiar de gestor. No traslada los registros entre bases de datos. Para producción también deben configurarse de forma segura otras opciones, como `SECRET_KEY`, `ALLOWED_HOSTS` y `DEBUG`.

### 4.6. Evitar que Git publique las credenciales

Añade al archivo `.gitignore` de la raíz del proyecto:

```gitignore
.env
.env.*
!.env.example
__pycache__/
*.py[cod]
.venv/
db.sqlite3
```

Es conveniente incluir un archivo `.env.example` con los nombres de las variables, pero **sin contraseñas reales**:

```dotenv
DB_ENGINE=postgresql
DB_NAME=biblioteca
DB_USER=biblioteca_user
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
DEBUG=False
```

Este archivo sí puede subirse a GitHub para documentar la configuración que necesita el proyecto. Cada estudiante puede copiarlo a `.env` y completar sus valores.

Si un archivo `.env` ya estaba siendo seguido por Git antes de añadirlo a `.gitignore`, la regla no lo elimina automáticamente del repositorio. Hay que dejar de rastrearlo y, si se han publicado credenciales reales, cambiarlas.

### 4.7. Probar el cambio de gestor

Con `DB_ENGINE=sqlite` en `.env`, ejecuta:

```bash
python manage.py migrate
python manage.py shell
```

En Django Shell:

```python
from django.db import connection
print(connection.vendor)
```

El resultado esperado es:

```text
sqlite
```

Después, cambia a `DB_ENGINE=postgresql` en `.env`, comprueba que PostgreSQL está funcionando y ejecuta nuevamente:

```bash
python manage.py migrate
python manage.py shell
```

```python
from django.db import connection
print(connection.vendor)
```

El resultado esperado es:

```text
postgresql
```

Cada ejecución de `manage.py` carga la configuración de nuevo. Si ya tienes una sesión de Django Shell abierta, ciérrala y vuelve a iniciarla después de modificar `.env`.

**Importante:** ejecutar `migrate` en PostgreSQL crea el **esquema**, pero no copia automáticamente los registros que ya existían en SQLite. Migrar datos entre gestores es un proceso diferente que requiere planificar la exportación e importación.

## 5. Otras configuraciones

Django utiliza el backend `django.db.backends.mysql` para MySQL y MariaDB. Se necesita instalar un controlador compatible y configurar `NAME`, `USER`, `PASSWORD`, `HOST` y `PORT` según el servidor. La compatibilidad concreta depende de la versión de Django y del gestor utilizado.

El mismo enfoque con `config()` permite recuperar estos parámetros desde variables de entorno.

## 6. Verificar la conexión

```bash
python manage.py check
python manage.py showmigrations catalogo
python manage.py migrate
python manage.py shell
```

Dentro de Django Shell:

```python
from django.db import connection
print(connection.vendor)
```

El resultado será `sqlite` o `postgresql`, según la configuración activa. `check` revisa la configuración del proyecto, pero no sustituye una prueba real de conexión a la base de datos.

## Actividad 9. Cambiar de gestor mediante variables de entorno

**Enunciado:** utiliza un mismo proyecto Django con dos gestores de bases de datos y gestiona su configuración mediante `python-decouple`.

1. Identifica los parámetros de conexión de SQLite en `settings.py`.
2. Instala `python-decouple` y utiliza `from decouple import config`.
3. Crea un archivo `.env` junto a `manage.py` y configura inicialmente `DB_ENGINE=sqlite`.
4. Añade `.env` a `.gitignore` y crea un archivo `.env.example` sin credenciales reales.
5. Modifica `settings.py` para seleccionar SQLite o PostgreSQL según el valor de `DB_ENGINE`.
6. Prepara una base de datos PostgreSQL local facilitada por el profesor o instalada previamente.
7. Instala el controlador `psycopg` y completa en `.env` las variables `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` y `DB_PORT`.
8. Cambia `DB_ENGINE` a `postgresql`, ejecuta `migrate` y comprueba que se han creado las tablas.
9. Consulta `connection.vendor` con cada gestor y documenta los resultados.
10. Utiliza `config("DEBUG", default=False, cast=bool)` y explica por qué se necesita `cast=bool`.
11. Explica por qué los datos existentes en SQLite no aparecen automáticamente en PostgreSQL.

**Entrega:** `settings.py`, `.gitignore`, `.env.example`, captura de las migraciones y explicación breve de las diferencias observadas. **No entregar el archivo `.env` con credenciales reales.**

**Preguntas:** ¿Qué diferencia hay entre `os.environ.get()` y `config()` de `python-decouple`? ¿Qué ocurre si se llama a `config("DB_PASSWORD")` y la variable no existe? ¿Por qué no se debe subir `.env` a GitHub? ¿Qué diferencia hay entre cambiar de gestor y migrar los datos?

**Siguiente bloque:** práctica integradora.
