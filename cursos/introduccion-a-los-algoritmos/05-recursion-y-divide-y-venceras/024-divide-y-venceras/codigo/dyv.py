# ep. 024 · Divide y vencerás
# Dividir, conquistar cada parte y combinar.
import math

llamadas = 0  # cuántas veces se llama la binaria
sumas = 0  # cuántas sumas hace suma_dyv


def busqueda_binaria_rec(lista, objetivo, lo, hi):
    global llamadas
    llamadas += 1
    if lo > hi:
        return -1  # caso base: no está
    mid = (lo + hi) // 2
    if lista[mid] == objetivo:
        return mid
    if lista[mid] < objetivo:  # sigue en la derecha
        return busqueda_binaria_rec(lista, objetivo,
                                    mid + 1, hi)
    return busqueda_binaria_rec(lista, objetivo,
                                lo, mid - 1)


def suma_dyv(lista):
    global sumas
    if len(lista) == 1:
        return lista[0]  # un elemento: esa es la suma
    if not lista:
        return 0  # vacía
    mitad = len(lista) // 2
    izquierda = suma_dyv(lista[:mitad])
    derecha = suma_dyv(lista[mitad:])
    sumas += 1  # combinar: una suma
    return izquierda + derecha


def mezclar(a, b):
    resultado = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # empate: gana a (estable)
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])  # una de las dos está vacía
    resultado.extend(b[j:])
    return resultado


def merge_sort(lista, nivel=0):
    if len(lista) <= 1:
        return lista  # ya está ordenada
    mitad = len(lista) // 2
    print("    " * nivel, lista[:mitad], lista[mitad:])
    izquierda = merge_sort(lista[:mitad], nivel + 1)
    derecha = merge_sort(lista[mitad:], nivel + 1)
    return mezclar(izquierda, derecha)


if __name__ == "__main__":
    precios = [3, 8, 12, 15, 21, 27, 33, 41, 52, 60]
    for objetivo in (41, 40):  # está / no está
        llamadas = 0
        pos = busqueda_binaria_rec(precios, objetivo,
                                   0, len(precios) - 1)
        print(objetivo, "->", pos, f"({llamadas} llamadas)")

    for n in (8, 1000):
        sumas = 0
        total = suma_dyv(list(range(1, n + 1)))
        print(f"suma_dyv de {n}: {total} con {sumas} sumas")

    numeros = [38, 27, 43, 3, 9, 82, 10, 5]
    print(numeros)
    print("->", merge_sort(numeros))
    print("niveles: log2(8) =", math.log2(len(numeros)))

    millon = list(range(1_000_000))
    llamadas = 0
    pos = busqueda_binaria_rec(millon, 777_777,
                               0, len(millon) - 1)
    print("binaria en 1.000.000:", llamadas, "llamadas")
