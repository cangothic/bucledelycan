import random
import timeit

alumnos = [("Ana", 9), ("Beto", 8), ("Caro", 9),
           ("Dani", 7), ("Eli", 8)]

if __name__ == "__main__":
    # Por nota, de mayor a menor: Ana y Caro no se cruzan
    por_nota = sorted(alumnos, key=lambda a: a[1],
                      reverse=True)
    print(por_nota)

    # Tupla: nota de mayor a menor; en empate, nombre A-Z
    por_tupla = sorted(alumnos, key=lambda a: (-a[1], a[0]))
    print(por_tupla)

    # Dos pasadas estables: primero nombre, luego nota
    primera = sorted(alumnos, key=lambda a: a[0])
    segunda = sorted(primera, key=lambda a: a[1],
                     reverse=True)
    print(segunda)
    print(por_nota == por_tupla == segunda)

    # sorted: lista nueva · sort: la misma, en su lugar
    lista = [9, 8, 9, 7, 8]
    print(sorted(lista), lista)
    lista.sort()
    print(lista)
    lista = lista.sort()  # error clásico
    print(lista)

    # Timsort: si ya viene ordenada, es un solo tramo
    ordenada = list(range(1_000_000))
    revuelta = ordenada[:]
    random.shuffle(revuelta)
    for nombre, datos in [("ordenada", ordenada),
                          ("revuelta", revuelta)]:
        t = min(timeit.repeat(lambda: sorted(datos),
                              number=1, repeat=3))
        print(nombre, round(t * 1000), "ms")
