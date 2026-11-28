# ep. 022 · Recursión sin miedo
# Caso base, acercarse a él y la pila de llamadas.
import sys


def saludar():
    print("hola")
    saludar()  # nada la detiene


def cuenta_regresiva(n):
    if n == 0:  # caso base
        print("despegue")
        return
    print(n)
    cuenta_regresiva(n - 1)  # se acerca al cero


def suma_lista(lista):
    if not lista:  # caso base: lista vacía
        return 0
    # lista[1:] copia el resto: con listas largas, tarda
    return lista[0] + suma_lista(lista[1:])


def suma_lista_pila(lista, nivel=0):
    sangria = "    " * nivel  # una sangría por llamada
    print(f"{sangria}suma({lista})")  # entra
    if not lista:
        print(f"{sangria}devuelve 0")  # sale
        return 0
    total = lista[0] + suma_lista_pila(lista[1:], nivel + 1)
    print(f"{sangria}devuelve {total}")  # sale
    return total


if __name__ == "__main__":
    try:
        saludar()
    except RecursionError as error:
        print("RecursionError:", error)

    cuenta_regresiva(3)
    assert suma_lista([1, 2, 3]) == 6
    suma_lista_pila([1, 2, 3])
    print(sys.getrecursionlimit())  # 1000 por defecto
