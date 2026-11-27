# ep. 020 · carrera de algoritmos: los cinco del módulo 4
# con 10, 1.000 y 100.000 datos; sorted() corre aparte.
import random
import timeit

from algoritmos import (burbuja, seleccion, insercion,
                        merge_sort, quick_sort)

algoritmos = {
    "burbuja": burbuja,
    "selección": seleccion,
    "inserción": insercion,
    "merge sort": merge_sort,
    "quick sort": quick_sort,
    "sorted": sorted,  # fuera de concurso: está en C
}
lentos = ("burbuja", "selección", "inserción")  # O(n²)

# por tamaño: veces que ordena en cada medida, y unidad
medidas = {
    10: (10000, "µs", 1e6),
    1000: (10, "ms", 1e3),
    100000: (1, "s", 1),
}


def medir(f, datos):
    # el mínimo de 3, dividido entre las veces (ep. 008)
    veces, _, escala = medidas[len(datos)]
    tiempos = timeit.repeat(lambda: f(datos),
                            number=veces, repeat=3)
    return min(tiempos) / veces * escala


def casi_ordenada(n):
    # todos en su lugar menos dos: el primero y el último
    datos = list(range(n))
    datos[0], datos[-1] = datos[-1], datos[0]
    return datos


def bonito(valor):
    # dos cifras y coma decimal: 0,40 · 2,5 · 63
    if valor is None:
        return "—"  # descalificado
    if valor >= 10:
        return f"{valor:.0f}"
    return f"{valor:#.2g}".rstrip(".").replace(".", ",")


def renglon(nombre, celdas):
    columnas = "".join(f"{c:>11}" for c in celdas)
    return f"{nombre:11}" + columnas


if __name__ == "__main__":
    random.seed(20)  # en cada corrida, los mismos datos
    carreras = {}
    for n in (10, 1000, 100000):
        datos = list(range(n))
        random.shuffle(datos)
        carreras[f"{n:,}".replace(",", ".")] = datos
    carreras["casi ord."] = casi_ordenada(1000)

    tabla = {nombre: {} for nombre in algoritmos}
    for titulo, datos in carreras.items():
        n = len(datos)
        for nombre, f in algoritmos.items():
            if n == 100000 and nombre in lentos:
                continue  # O(n²): ~15 min entre los tres
            tabla[nombre][titulo] = medir(f, datos)

    print(renglon("", carreras))
    print(renglon("", [medidas[len(d)][1]
                       for d in carreras.values()]))
    for nombre, tiempos in tabla.items():
        print(renglon(nombre, [bonito(tiempos.get(t))
                               for t in carreras]))
    print("sorted: fuera de concurso, está escrito en C.")
    print("—: O(n²) con 100.000 datos, descalificado.")
