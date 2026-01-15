## 1) Paginación en CBV (ListView) 

1. Usa `ListView`.
2. Define `paginate_by`.
3. En plantilla, usa `page_obj` y `paginator`.

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    paginate_by = 10
```

Plantilla (mínimo):

```django
{% for post in object_list %}
  {{ post.title }}
{% endfor %}

{% if is_paginated %}
  {% if page_obj.has_previous %}
    <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
  {% endif %}

  Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}

  {% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">Siguiente</a>
  {% endif %}
{% endif %}
```

---

## 2) Paginación en FBV (function-based view) con `Paginator`

1. Importa `Paginator`.
2. Crea el queryset.
3. Lee `page` de `request.GET`.
4. Pasa `page_obj` a la plantilla.

```python
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all().order_by("-id")
    paginator = Paginator(qs, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "posts/list.html", {"page_obj": page_obj})
```

Plantilla:

```django
{% for post in page_obj %}
  {{ post.title }}
{% endfor %}

{% if page_obj.has_previous %}
  <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
{% endif %}

{{ page_obj.number }} / {{ page_obj.paginator.num_pages }}

{% if page_obj.has_next %}
  <a href="?page={{ page_obj.next_page_number }}">Siguiente</a>
{% endif %}
```

---

## 3) Mantener filtros/queries (búsqueda, ordering) al paginar

1. Mantén `?search=...&page=...`
2. En plantilla, reusa `request.GET.urlencode` (o construye la query sin `page`).

Atajo típico:

```django
<a href="?{{ request.GET.urlencode }}&page={{ page_obj.next_page_number }}">Siguiente</a>
```

*(Ojo: esto puede duplicar `page`; lo “fino” es quitar `page` antes.) ¿Cómo se puede solucionar?*

---

## 4) Si es Django REST Framework (API)

1. Activa paginación en `settings.py` o por vista.
2. Define `PAGE_SIZE`.

```python
REST_FRAMEWORK = {
  "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
  "PAGE_SIZE": 10,
}
```

