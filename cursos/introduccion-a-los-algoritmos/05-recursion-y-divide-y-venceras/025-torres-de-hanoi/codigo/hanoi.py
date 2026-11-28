# ep. 025 · Torres de Hanói
# Quita n − 1 del camino, mueve el grande, ponlos encima.


def hanoi(n, origen, destino, auxiliar):
    if n == 0:
        return  # cero discos: no hay nada que mover
    hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mueve disco {n} de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen)


def contar(n):
    # Lo mismo que hanoi, con un contador en vez de print.
    if n == 0:
        return 0
    return contar(n - 1) + 1 + contar(n - 1)


if __name__ == "__main__":
    hanoi(3, "A", "C", "B")
    print([contar(n) for n in range(1, 11)])
