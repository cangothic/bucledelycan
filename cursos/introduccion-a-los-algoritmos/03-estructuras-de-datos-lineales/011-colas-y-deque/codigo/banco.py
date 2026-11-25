import timeit
from collections import deque


def atender_con_lista(n):
    fila = list(range(n))  # n clientes formados
    while fila:
        fila.pop(0)  # atiende al primero: todos se recorren


def atender_con_deque(n):
    fila = deque(range(n))
    while fila:
        fila.popleft()  # atiende al primero: nadie se mueve


for n in [100_000, 200_000]:
    li = min(timeit.repeat(lambda: atender_con_lista(n), number=1, repeat=3))
    de = min(timeit.repeat(lambda: atender_con_deque(n), number=1, repeat=3))
    print(n, "lista", round(li, 2), "s · deque", round(de, 4), "s")

fila = deque()
for cliente in ["Ana", "Beto", "Caro"]:
    fila.append(cliente)  # llegan al final
print("atiende a", fila.popleft())
fila.append("Dani")
print("atiende a", fila.popleft())
