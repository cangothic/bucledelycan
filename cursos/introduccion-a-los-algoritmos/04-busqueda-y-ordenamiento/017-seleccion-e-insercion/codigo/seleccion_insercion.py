# ep. 017 · Selección e inserción
# Dos O(n²) que con los mismos datos se portan distinto.
import random


def seleccion(lista):
    lista, comps = lista[:], 0  # copia y contador
    n = len(lista)
    for i in range(n - 1):
        menor = i  # supongo que el menor está en i
        for j in range(i + 1, n):  # recorro el resto
            comps += 1
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista, comps


def insercion(lista):
    lista, comps = lista[:], 0  # copia y contador
    for i in range(1, len(lista)):
        carta = lista[i]
        j = i - 1  # empieza a su izquierda
        while j >= 0 and lista[j] > carta:
            comps += 1
            lista[j+1] = lista[j]  # se recorre a la derecha
            j -= 1
        if j >= 0:
            comps += 1  # la comparación que la detuvo
        lista[j+1] = carta
    return lista, comps


if __name__ == "__main__":
    random.seed(17)  # el mismo azar en cada corrida
    ordenada = list(range(1000))
    al_azar = random.sample(ordenada, 1000)
    al_reves = ordenada[::-1]
    casos = {"ordenada": ordenada, "al azar": al_azar,
             "al revés": al_reves}
    for nombre, ordena in [("selección", seleccion),
                           ("inserción", insercion)]:
        for caso, datos in casos.items():
            resultado, comps = ordena(datos)
            assert resultado == sorted(datos)
            miles = f"{comps:,}".replace(",", ".")
            print(f"{nombre}  {caso:9}{miles:>8}")
    assert al_reves[0] == 999  # la original no se toca
