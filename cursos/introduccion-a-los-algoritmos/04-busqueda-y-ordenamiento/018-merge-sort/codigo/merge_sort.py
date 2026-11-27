# ep. 018 · Merge sort
# Parte a la mitad, ordena cada mitad y mezcla.
import random
import timeit


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


def merge_sort(lista):
    if len(lista) <= 1:
        return lista  # ya está ordenada
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])
    return mezclar(izquierda, derecha)


if __name__ == "__main__":
    numeros = [38, 27, 43, 3, 9, 82, 10]
    print(numeros, "->", merge_sort(numeros))

    random.seed(18)
    datos = list(range(100_000))
    random.shuffle(datos)  # 100.000 números al azar
    assert merge_sort(datos) == sorted(datos)
    tiempos = timeit.repeat(lambda: merge_sort(datos),
                            number=1, repeat=5)
    print(f"100.000 aleatorios: {min(tiempos):.2f} s")
