# ep. 008 · lo que se mide en medir.py: los dos tiene_repetidos del ep. 005 y una suma con for.


def tiene_repetidos(lista):
    # dos ciclos: compara cada pareja una vez, O(n²)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


def tiene_repetidos_con_set(lista):
    # un conjunto guarda cada elemento una sola vez: si queda más corto, había repetidos. O(n)
    return len(set(lista)) != len(lista)


def suma_con_for(numeros):
    total = 0
    for x in numeros:
        total += x
    return total
