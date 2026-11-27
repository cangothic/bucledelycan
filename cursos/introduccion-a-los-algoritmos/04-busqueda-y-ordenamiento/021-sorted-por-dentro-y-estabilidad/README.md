# // ep. 021 · sorted() en Python por dentro: cómo ordenar listas con key, reverse y estabilidad

**Curso:** [Introducción a los Algoritmos](../../) · **Módulo 4 — Búsqueda y ordenamiento** · estreno el 12 mar 2027

Ordenas a tus alumnos por calificación y los que empatan quedan en orden alfabético, sin que se lo pidas a Python. ¿Casualidad? No: es una propiedad que tiene nombre, la estabilidad, y te ahorra mucho código. Hoy vemos qué hace sorted() por dentro y cómo usar key, reverse y la estabilidad para ordenar por varios criterios a la vez.

| Archivo | Qué es |
| --- | --- |
| [codigo/ordenar_alumnos.py](codigo/ordenar_alumnos.py) | El código del video. Ejecútalo con `python codigo/ordenar_alumnos.py` |

## Fuentes

- Documentación de Python, «Sorting Techniques» (los ordenamientos son estables, key, y reverse conserva la estabilidad): https://docs.python.org/es/3/howto/sorting.html
- Tim Peters, listsort.txt en el código de CPython (Timsort, 2002; desde Python 3.11 elige qué tramos mezclar con «powersort», de Munro y Wild): https://github.com/python/cpython/blob/main/Objects/listsort.txt
