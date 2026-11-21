from cajon import buscar_uno_por_uno, cajon
import sys

pasos = [buscar_uno_por_uno(cajon, c)[1]
         for c in cajon]
print("promedio =", sum(pasos) / len(pasos))
print("mínimo:", min(pasos), "máximo:", max(pasos))
print("de lunares:", buscar_uno_por_uno(cajon, "de lunares")[1])

numeros = list(range(1_000_000))
print(sys.getsizeof(numeros))       # la lista
print(sys.getsizeof(set(numeros)))  # el conjunto
