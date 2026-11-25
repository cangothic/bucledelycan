class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # todavía no apunta a nadie


def insertar_al_inicio(cabeza, valor):
    nuevo = Nodo(valor)
    nuevo.siguiente = cabeza  # apunta a la cabeza actual
    return nuevo              # y se vuelve la nueva cabeza


def recorrer(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual.valor, end=" -> ")
        actual = actual.siguiente
    print(None)


def buscar(cabeza, objetivo):
    actual = cabeza
    while actual is not None:
        if actual.valor == objetivo:
            return True
        actual = actual.siguiente
    return False


def longitud(cabeza):
    n = 0
    actual = cabeza
    while actual is not None:  # hay que contarlos: O(n)
        n += 1
        actual = actual.siguiente
    return n


cabeza = None
for valor in [3, 2, 1]:
    cabeza = insertar_al_inicio(cabeza, valor)
recorrer(cabeza)
print(buscar(cabeza, 2))
print(longitud(cabeza))
