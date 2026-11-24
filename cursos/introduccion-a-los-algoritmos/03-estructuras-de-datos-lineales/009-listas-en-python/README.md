# // ep. 009 · Listas en Python: lo que cuesta cada operación (append, insert y Big O)

**Curso:** [Introducción a los Algoritmos](../../) · **Módulo 3 — Estructuras de datos lineales** · estreno el 18 dic 2026

Agrego cien mil elementos al final de una lista: 8 milésimas de segundo. Los mismos cien mil, pero al principio: 2,4 segundos. Trescientas veces más lento, con la misma lista y los mismos datos. ¿Por qué?

| Archivo | Qué es |
| --- | --- |
| [codigo/listas.py](codigo/listas.py) | El código del video. Ejecútalo con `python codigo/listas.py` |

## Fuentes

- Python Wiki, «TimeComplexity» (lo que cuesta cada operación de list, y append amortizado): https://wiki.python.org/moin/TimeComplexity
- Documentación de Python, sys.getsizeof(): https://docs.python.org/es/3/library/sys.html#sys.getsizeof
