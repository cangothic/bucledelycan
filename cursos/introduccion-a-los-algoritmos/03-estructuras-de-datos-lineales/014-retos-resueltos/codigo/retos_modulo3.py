from collections import Counter


def balanceados(texto):
    pares = {")": "(", "]": "[", "}": "{"}
    pila = []
    for simbolo in texto:
        if simbolo in "([{":
            pila.append(simbolo)
        elif simbolo in pares:
            if not pila or pila.pop() != pares[simbolo]:
                return False
    return not pila


def frecuencias(texto):
    palabras = [p.strip('.,;:¡!¿?«»"()') for p in texto.lower().split()]
    return Counter(p for p in palabras if p)


print(balanceados("print((2+3)*(4)"))
print(balanceados("{[()]}"), balanceados("{[(])}"))

parrafo = """La pila guarda lo último que llega y lo saca primero. La cola,
en cambio, atiende primero al que llegó antes. Con un diccionario
cuentas las palabras de un texto en una sola pasada, y con un
conjunto sabes al instante si ya viste algo. Elegir la estructura
es la mitad del trabajo: la otra mitad es que el código se lea fácil."""
print(frecuencias(parrafo).most_common(3))
