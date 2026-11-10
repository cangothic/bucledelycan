import calendar


def mayor(lista):
    if not lista:
        return None
    el_mayor = lista[0]
    for numero in lista[1:]:
        if numero > el_mayor:
            el_mayor = numero
    return el_mayor


def contar_vocales(texto, vocales="aeiouáéíóúü"):
    contador = 0
    for letra in texto.lower():
        if letra in vocales:
            contador += 1
    return contador


def es_bisiesto(año):
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    return año % 4 == 0


if __name__ == "__main__":
    print(mayor([3, 8, 2, 9, 4]), mayor([-5, -2]), mayor([]))
    print(contar_vocales("murciélago"), contar_vocales("Ánimo"), contar_vocales("pingüino"))
    for año in (2024, 2023, 1900, 2000):
        print(f"es_bisiesto({año}): {es_bisiesto(año)}")
    iguales = all(es_bisiesto(año) == calendar.isleap(año) for año in range(1, 3001))
    print("del año 1 al 3000, igual que calendar.isleap:", iguales)
