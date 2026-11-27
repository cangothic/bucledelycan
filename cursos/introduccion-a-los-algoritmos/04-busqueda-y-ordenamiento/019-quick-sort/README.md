# // ep. 019 · Quicksort en Python: ordenamiento rápido y por qué importa el pivote

**Curso:** [Introducción a los Algoritmos](../../) · **Módulo 4 — Búsqueda y ordenamiento** · estreno el 26 feb 2027

Hay un algoritmo que se llama, literalmente, «ordenamiento rápido», y puede ser tan lento como burbuja en su peor caso. Lo más raro: le pasa justo cuando la lista ya está ordenada. Hoy programamos quick sort en Python y vemos por qué todo depende de una sola decisión: el pivote.

| Archivo | Qué es |
| --- | --- |
| [codigo/quick_sort.py](codigo/quick_sort.py) | El código del video. Ejecútalo con `python codigo/quick_sort.py` |

## Fuentes

- C. A. R. Hoare, «Quicksort», The Computer Journal, 5(1), 1962, pp. 10–16 (el algoritmo es de 1959): https://doi.org/10.1093/comjnl/5.1.10
- Documentación de Python: sys.setrecursionlimit (el límite por defecto, 1.000): https://docs.python.org/es/3/library/sys.html#sys.setrecursionlimit
