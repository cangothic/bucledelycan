import timeit

print(hash("hola"))  # cambia en cada ejecución
print(hash(7))       # un entero pequeño: el mismo número

def tiene_repetidos(lista):
    vistos = set()
    for x in lista:
        if x in vistos:
            return True  # termina en el primer repetido
        vistos.add(x)
    return False

print(tiene_repetidos([3, 1, 4, 1, 5]))

contar = {}
for palabra in "el gato y el perro y el pez".split():
    contar[palabra] = contar.get(palabra, 0) + 1
print(contar)

numeros = list(range(1_000_000))
conjunto = set(numeros)
li = min(timeit.repeat(lambda: 999_999 in numeros, number=10)) / 10
co = min(timeit.repeat(lambda: 999_999 in conjunto, number=10**5)) / 10**5
print("lista", round(li * 1000, 1), "ms · set", round(co * 1e9), "ns")
