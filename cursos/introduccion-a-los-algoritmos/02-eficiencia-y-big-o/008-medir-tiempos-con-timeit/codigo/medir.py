import timeit
from repetidos import (tiene_repetidos, tiene_repetidos_con_set,
                       suma_con_for)

for n in [1000, 2000, 4000]:
    datos = list(range(n))  # sin repetidos: el peor caso
    tiempos = timeit.repeat(lambda: tiene_repetidos(datos),
                            number=1, repeat=3)
    print("doble ciclo", n, round(min(tiempos) / 1, 3), "s")

for n in [1000, 2000, 4000]:
    datos = list(range(n))
    tiempos = timeit.repeat(lambda: tiene_repetidos_con_set(datos),
                            number=1000, repeat=3)
    print("set", n, round(min(tiempos) / 1000 * 1e6), "µs")

numeros = list(range(1_000_000))
con_for = timeit.repeat(lambda: suma_con_for(numeros),
                        number=10, repeat=3)
con_sum = timeit.repeat(lambda: sum(numeros), number=10, repeat=3)
print("for", round(min(con_for) / 10 * 1000), "ms")
print("sum", round(min(con_sum) / 10 * 1000), "ms")
