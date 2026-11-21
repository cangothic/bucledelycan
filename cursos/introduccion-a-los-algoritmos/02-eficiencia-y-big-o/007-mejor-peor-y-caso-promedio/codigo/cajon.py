def buscar_uno_por_uno(cajon, buscado):
    """El mismo algoritmo que buscar_gol_minuto_a_minuto del ep. 001, con calcetines.
    Entrada: los calcetines del cajón, en el orden en que los sacas, y el que buscas.
    Salida: en qué posición estaba (-1 si no está) y cuántos sacaste."""
    pasos = 0
    for posicion in range(len(cajon)):
        pasos += 1
        if cajon[posicion] == buscado:
            return posicion, pasos
    return -1, pasos


# 24 calcetines sueltos: el rojo adelante y el de rayas al fondo. El de lunares no está (se perdió en la lavadora).
cajon = ["rojo", "azul", "verde", "negro", "blanco", "gris", "amarillo", "naranja", "morado", "rosado", "café", "beige",
         "vinotinto", "turquesa", "azul oscuro", "verde claro", "de cuadros", "de estrellas", "de dinosaurios", "de corazones",
         "de fútbol", "navideño", "de lycan", "de rayas"]


if __name__ == "__main__":
    for calcetin in ["rojo", "de rayas", "de lunares"]:
        posicion, pasos = buscar_uno_por_uno(cajon, calcetin)
        print(f"{calcetin} → posición: {posicion}, pasos: {pasos}")

    assert len(cajon) == 24 and len(set(cajon)) == 24
    assert buscar_uno_por_uno(cajon, "rojo") == (0, 1)
    assert buscar_uno_por_uno(cajon, "de rayas") == (23, 24)
    assert buscar_uno_por_uno(cajon, "de lunares") == (-1, 24)
    assert buscar_uno_por_uno([], "rojo") == (-1, 0)
    print("Todos los casos pasan.")
