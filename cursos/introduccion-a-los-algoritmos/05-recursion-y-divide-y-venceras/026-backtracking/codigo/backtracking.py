# ep. 026 · Backtracking
# Elegir, explorar, deshacer.


def permutaciones(restantes, actual=""):
    if not restantes:
        print(actual)  # no quedan letras
        return
    for i, letra in enumerate(restantes):
        quedan = restantes[:i] + restantes[i + 1:]
        permutaciones(quedan, actual + letra)
        # al regresar, el for prueba la siguiente letra


def resolver(lab, f, c, visitado, camino):
    if not (0 <= f < len(lab) and 0 <= c < len(lab[0])):
        return False  # fuera del laberinto
    if lab[f][c] == "#" or (f, c) in visitado:
        return False  # pared o ya visitada: poda
    if lab[f][c] == "E":
        camino.append((f, c))
        return True  # la salida
    visitado.add((f, c))
    camino.append((f, c))  # avanzar: append
    for df, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if resolver(lab, f + df, c + dc, visitado, camino):
            return True
    camino.pop()  # callejón: retroceder es pop
    return False


def dibujar(lab, camino):
    for f, fila in enumerate(lab):
        linea = ""
        for c, casilla in enumerate(fila):
            if casilla == "." and (f, c) in camino:
                casilla = "*"
            linea += casilla
        print(linea)


if __name__ == "__main__":
    permutaciones("abc")

    laberinto = [
        "S..#......",
        ".#.#.####.",
        ".#...#....",
        ".####.#.#.",
        "......#.#E",
    ]
    camino = []
    print(resolver(laberinto, 0, 0, set(), camino))
    dibujar(laberinto, camino)

    tapado = [fila.replace("E", "#") for fila in laberinto]
    print("salida tapada:",
          resolver(tapado, 0, 0, set(), []))
