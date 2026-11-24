import sys
import timeit


def con_append(n):
    lista = []
    for i in range(n):
        lista.append(i)  # al final
    return lista


def con_insert(n):
    lista = []
    for i in range(n):
        lista.insert(0, i)  # al principio
    return lista


for n in [50_000, 100_000]:
    ap = min(timeit.repeat(lambda: con_append(n), number=1, repeat=3))
    ins = min(timeit.repeat(lambda: con_insert(n), number=1, repeat=3))
    print(n, "append", round(ap, 3), "s · insert", round(ins, 1), "s")

lista = []
tamano = sys.getsizeof(lista)
for i in range(1, 41):
    lista.append(i)
    nuevo = sys.getsizeof(lista)
    if nuevo != tamano:  # se mudó
        print("con", len(lista), "->", nuevo, "bytes")
        tamano = nuevo
