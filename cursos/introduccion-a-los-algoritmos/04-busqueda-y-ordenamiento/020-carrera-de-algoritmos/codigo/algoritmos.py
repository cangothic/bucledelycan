# ep. 020 · los cinco corredores: las versiones sencillas
# de los eps. 016 a 019, en Python puro y sin contadores.
# Ninguno toca la lista original.
import random


def burbuja(lista):
    lista = lista[:]  # una copia: la original no se toca
    n = len(lista)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return lista


def seleccion(lista):
    lista = lista[:]
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


def insercion(lista):
    lista = lista[:]
    for i in range(1, len(lista)):
        carta = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > carta:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = carta
    return lista


def mezclar(a, b):
    resultado = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])
    return mezclar(izquierda, derecha)


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = random.choice(lista)
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return (quick_sort(menores) + iguales
            + quick_sort(mayores))


if __name__ == "__main__":
    prueba = [38, 27, 43, 3, 9, 82, 10, 27]
    for f in (burbuja, seleccion, insercion,
              merge_sort, quick_sort):
        assert f(prueba) == sorted(prueba)
        assert f([]) == [] and f([7]) == [7]
        assert f([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert prueba == [38, 27, 43, 3, 9, 82, 10, 27]
    print("Los cinco ordenan bien.")
