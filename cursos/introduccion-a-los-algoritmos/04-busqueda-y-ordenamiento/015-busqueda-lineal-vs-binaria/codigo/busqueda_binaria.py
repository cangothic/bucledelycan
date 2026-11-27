from bisect import bisect_left


def busqueda_binaria(lista, objetivo):
    lo, hi = 0, len(lista) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lista[mid] == objetivo:
            return mid
        if lista[mid] < objetivo:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    precios = [3, 8, 12, 15, 21, 27, 33, 41, 52, 60]
    print(busqueda_binaria(precios, 41))  # está
    print(busqueda_binaria(precios, 40))  # no está
    print(bisect_left(precios, 41))  # dónde está
    print(bisect_left(precios, 40))  # dónde iría
