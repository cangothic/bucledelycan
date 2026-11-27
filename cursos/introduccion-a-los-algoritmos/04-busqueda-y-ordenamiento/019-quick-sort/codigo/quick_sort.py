# ep. 019 · Quick sort
# Elige un pivote y separa menores, iguales y mayores.
import random
import sys

sys.setrecursionlimit(3000)  # 1.000 llamadas anidadas


def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # ya está ordenada
    pivote = random.choice(lista)
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return (quick_sort(menores) + iguales
            + quick_sort(mayores))


comparaciones = 0


def quick_sort_contado(lista, al_azar):
    global comparaciones
    if len(lista) <= 1:
        return lista
    if al_azar:
        pivote = random.choice(lista)
    else:
        pivote = lista[0]  # siempre el primero
    # cada uno de los demás se compara con el pivote
    comparaciones += len(lista) - 1
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return (quick_sort_contado(menores, al_azar) + iguales
            + quick_sort_contado(mayores, al_azar))


if __name__ == "__main__":
    random.seed(19)
    numeros = [33, 8, 51, 12, 47, 3, 29, 29]
    esperado = sorted(numeros)
    assert quick_sort(numeros) == esperado
    assert quick_sort_contado(numeros, False) == esperado
    assert quick_sort_contado(numeros, True) == esperado

    ordenados = list(range(1000))
    print("1.000 ordenados")
    comparaciones = 0
    quick_sort_contado(ordenados, al_azar=False)
    print("pivote primero:", comparaciones)
    for intento in range(3):
        comparaciones = 0
        quick_sort_contado(ordenados, al_azar=True)
        print("pivote al azar:", comparaciones)
