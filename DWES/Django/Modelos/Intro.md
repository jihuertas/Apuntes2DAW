# Persistencia – Introducción a los Modelos en Django

Veamos cómo funcionan los **modelos en Django**, analizando los tipos de campos más utilizados y más adelante explicaremos de forma detallada las relaciones entre modelos: `OneToOne`, `ForeignKey` y `ManyToMany`.

---

## ¿Qué es un Modelo en Django?

Un modelo es una clase de Python que define la estructura de los datos que queremos almacenar. Django utiliza estos modelos para crear tablas en la base de datos y gestionar la información mediante su sistema de ORM (aunque aquí no lo trabajaremos).

Un modelo se suele declarar así:

```python
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    paginas = models.IntegerField()
```

---

# Tipos de Campos Más Comunes

Django ofrece una gran variedad de tipos de campos. Aquí se explican los más importantes y utilizados.

## Campos de Texto

* **CharField(max_length=…):**
  Para textos cortos como nombres o títulos. Requiere un valor máximo de caracteres.
* **TextField():**
  Para textos largos, como descripciones o artículos completos.

## Campos Numéricos

* **IntegerField():**
  Para números enteros.
* **FloatField():**
  Permite almacenar números decimales con coma flotante.
* **DecimalField(max_digits=…, decimal_places=…):**
  Para números decimales de precisión fija (ideal para dinero o notas).

## Campos de Fecha y Hora

* **DateField():**
  Guarda una fecha.
* **DateTimeField():**
  Guarda fecha y hora exacta.

## Campos Booleanos

* **BooleanField():**
  Guarda valores verdadero/falso.

## Campos para Archivos

* **FileField(upload_to=…):**
  Para almacenar archivos (PDF, documentos…).
* **ImageField(upload_to=…):**
  Para imágenes (requiere instalar la librería *Pillow*).


