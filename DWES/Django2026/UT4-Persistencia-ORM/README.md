# UT4. Persistencia: bases de datos y ORM

## Descripción

En esta unidad aprenderemos a gestionar la persistencia de información en aplicaciones web mediante bases de datos relacionales y el mapeo objeto-relacional (ORM) de Django. Definiremos modelos, aplicaremos migraciones, realizaremos operaciones CRUD y consultas, relacionaremos entidades y utilizaremos transacciones y el panel de administración. También configuraremos Django con distintos sistemas gestores de bases de datos.

Los materiales están organizados en diez bloques. Se recomienda seguir el orden propuesto y mantener el mismo proyecto Django `biblioteca` durante las prácticas.

## Contenidos y materiales

| Bloque | Contenidos | Duración | Material |
|---|---|---:|---|
| 1 | Persistencia y bases de datos relacionales; configuración inicial de Django | [Acceder](01-persistencia-bases-datos.md) |
| 2 | ORM, definición de modelos, tipos de campos y restricciones | Acceder](02-modelos-orm.md) |
| 3 | Creación y aplicación de migraciones | [Acceder](03-migraciones.md) |
| 4 | Operaciones CRUD; recuperación y modificación de información | [Acceder](04-operaciones-crud.md) |
| 5 | Consultas ORM: filtrado, ordenación y agregación | [Acceder](05-consultas-orm.md) |
| 6 | Relaciones entre modelos: uno a uno, uno a muchos y muchos a muchos | [Acceder](06-relaciones-modelos.md) |
| 7 | Integridad de datos y transacciones | [Acceder](07-integridad-transacciones.md) |
| 8 | Panel de administración de Django | [Acceder](08-panel-administracion.md) |
| 9 | Configuración con diferentes gestores de bases de datos | [Acceder](09-gestores-bases-datos.md) |
| 10 | Práctica integradora: gestión de modelos relacionados | [Acceder](10-practica-integradora.md) |


## Objetivos de aprendizaje

- Comprender la persistencia de datos en aplicaciones web y el modelo relacional.
- Configurar bases de datos en Django.
- Definir modelos con campos, restricciones y relaciones.
- Generar, aplicar y revisar migraciones.
- Realizar operaciones CRUD y consultas mediante el ORM.
- Filtrar, ordenar y agregar resultados.
- Mantener la integridad de los datos y utilizar transacciones.
- Gestionar modelos desde Django Admin.
- Configurar el proyecto con distintos gestores relacionales.

## Actividades de enseñanza-aprendizaje

1. Creación de modelos Django.
2. Generación y aplicación de migraciones.
3. Prácticas de consultas utilizando el ORM.
4. Realización de operaciones CRUD.
5. Diseño de modelos relacionados mediante diferentes tipos de relaciones.
6. Utilización del panel de administración.
7. Desarrollo de aplicaciones que gestionen modelos relacionados de cierta complejidad.
8. Configuración de proyectos Django con diferentes gestores de bases de datos.

## Herramientas

- Python y Django.
- SQLite y PostgreSQL.
- Visual Studio Code u otro editor.
- DB Browser for SQLite (opcional).
- Git y GitHub.

## Organización del repositorio

```text
UT4-Persistencia-ORM/
├── README.md
├── 01-persistencia-bases-datos.md
├── 02-modelos-orm.md
├── 03-migraciones.md
├── 04-operaciones-crud.md
├── 05-consultas-orm.md
├── 06-relaciones-modelos.md
├── 07-integridad-transacciones.md
├── 08-panel-administracion.md
├── 09-gestores-bases-datos.md
└── 10-practica-integradora.md
```

Todos los enlaces son relativos y funcionan cuando los archivos están en la misma carpeta del repositorio de GitHub.

## Proyecto de trabajo

Las prácticas se desarrollan sobre un proyecto Django denominado `biblioteca`, con una aplicación `catalogo`. Se comienza configurando la base de datos y definiendo modelos; posteriormente se incorporan consultas, relaciones, préstamos, transacciones y administración. La última actividad integra los contenidos de toda la unidad.
