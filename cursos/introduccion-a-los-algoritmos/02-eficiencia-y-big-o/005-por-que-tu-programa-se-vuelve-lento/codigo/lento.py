# ep. 005 · ¿Por qué tu programa se vuelve lento?
# El mismo código con 1.000, 2.000 y 4.000 datos: cuenta las comparaciones y mide el tiempo.
import time


def tiene_repetidos(lista):
    comparaciones = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparaciones += 1
            if lista[i] == lista[j]:
                return True, comparaciones
    return False, comparaciones


def tiene_repetidos_con_set(lista):
    # un conjunto guarda cada elemento una sola vez: si queda más corto, había repetidos
    return len(set(lista)) != len(lista)


for n in [1000, 2000, 4000]:
    datos = list(range(n))  # sin repetidos
    inicio = time.perf_counter()
    _, comps = tiene_repetidos(datos)
    print(n, comps, time.perf_counter() - inicio)

# la versión con set, con los mismos datos y con un millón
for n in [1000, 2000, 4000, 1_000_000]:
    datos = list(range(n))
    inicio = time.perf_counter()
    tiene_repetidos_con_set(datos)
    print('set', n, time.perf_counter() - inicio)
