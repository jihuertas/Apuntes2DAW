En [la solución del ejercicio anterior](https://github.com/jihuertas/gestioncursos/blob/solucionJI/cursosapp/templates/cursosapp/base.html) habrás comprobado que en los templates se han incluido algunos estilos que hacen que las páginas se muestren mejor.

A continuación vamos a ver en qué consisten los cambios introducidos:

Las modificaciones principales están en el archivo `base.html`, donde se han integrado varios estilos utilizando Bootstrap para estructurar la plantilla base en dos partes: un menú lateral y una sección de contenido principal. Veamos cómo funcionan los estilos y las clases usadas:

---

### **0. Integración de Bootstrap**
- Dentro del bloque <head> hay que añadir el archivo CSS de Bootstrap (hemos usado la última versión existente al escribir estos apuntes, pero [puedes ver la más actual aquí](https://getbootstrap.com/docs/5.3/getting-started/download/)
- Puedes hacerlo de distintas formas. En nuestro caso hemos enlazado desde un CDN (Content Delivery Network) para usar sus clases y estilos.
- Te recomendamos añadir el CSS dentro del head, y el archivo JS de Bootstrap (para funcionalidades como menús desplegables o modales) justo al final del body.
```html
<head>
<!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
<!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

```

---


### **1. Contenedor principal**
```html
<div class="container-fluid">
```
- **`container-fluid`:** Este contenedor abarca todo el ancho de la pantalla, útil para diseños donde quieres aprovechar todo el espacio horizontal.

---

### **2. Estructura de fila**
```html
<div class="row">
```
- **`row`:** Es un contenedor para agrupar columnas en Bootstrap. Las filas dividen el espacio en una estructura de 12 columnas por defecto.

---

### **3. Menú lateral (sidebar)**
```html
<nav class="col-md-2 d-none d-md-block bg-light sidebar">
```
- **`col-md-2`:** Asigna un ancho de 2 columnas (de 12 disponibles) al menú lateral en dispositivos medianos o más grandes.
- **`d-none d-md-block`:** Oculta el menú lateral en dispositivos pequeños y lo muestra solo en dispositivos medianos o mayores.
- **`bg-light`:** Aplica un fondo claro al menú lateral.
- **`sidebar`:** Una clase personalizada (no propia de Bootstrap). Puedes usarla para aplicar estilos adicionales en un archivo CSS.

```html
<ul class="nav flex-column">
    <li class="nav-item">
        <a class="nav-link active" href="{% url 'lista_cursos' %}">Cursos</a>
    </li>
</ul>
```
- **`nav flex-column`:** Define una lista de navegación vertical en lugar de horizontal.
- **`nav-item` y `nav-link`:** Clases de Bootstrap para estilizar elementos de navegación.
- **`active`:** Indica que el enlace actual está activo, aplicando un estilo distintivo.

---

### **4. Contenido principal**
```html
<main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
```
- **`col-md-9`:** Asigna 9 columnas de ancho al contenido principal en dispositivos medianos o mayores (el menú ocupa las otras 3 columnas restantes).
- **`ms-sm-auto`:** Agrega un margen automático en el lado izquierdo para dispositivos pequeños o mayores, asegurando que el contenido esté correctamente alineado.
- **`col-lg-10`:** En pantallas grandes, el contenido principal ocupa 10 columnas (el menú lateral se reduce).
- **`px-md-4`:** Agrega un relleno horizontal (padding) de 4 unidades en dispositivos medianos o mayores.



---

### **5. Resultado **
- **Diseño responsivo:** El menú lateral aparece en dispositivos medianos o más grandes, mientras que el contenido principal se adapta dinámicamente.
- **Estilo moderno y claro:** Gracias a las clases de Bootstrap, se obtiene un diseño limpio y bien alineado sin necesidad de crear CSS personalizado desde cero.
