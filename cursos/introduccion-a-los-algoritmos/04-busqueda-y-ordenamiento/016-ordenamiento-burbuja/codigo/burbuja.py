# ep. 016 · Ordenamiento burbuja
# Compara vecinos y los intercambia si están al revés.
import random
import timeit


def burbuja(lista):
    lista = lista[:]  # una copia: la original no se toca
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    for i in range(n - 1):  # las pasadas
        hubo_intercambio = False
        for j in range(n - 1 - i):  # los últimos i ya están
            comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambios += 1
                hubo_intercambio = True
        if not hubo_intercambio:
            break  # ya está ordenada
    return lista, comparaciones, intercambios


if __name__ == "__main__":
    original = [5, 4, 3, 2, 1]
    lista, comps, inter = burbuja(original)
    print(original, "->", lista)
    print(comps, "comparaciones,", inter, "intercambios")

    _, comps, inter = burbuja(list(range(1000)))
    print("1.000 ordenados:", comps, "comparaciones,",
          inter, "intercambios")

    datos = list(range(2000))
    random.shuffle(datos)  # 2.000 números al azar
    assert burbuja(datos)[0] == sorted(datos)
    tiempos = timeit.repeat(lambda: burbuja(datos),
                            number=1, repeat=5)
    print("2.000 aleatorios:", round(min(tiempos), 2), "s")
