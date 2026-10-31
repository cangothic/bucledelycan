# La búsqueda del gol del ep. 001 con el truco del ep. 002: primero el pseudocódigo como comentarios,
# y debajo de cada comentario, su línea de Python.


# RECIBE el partido: el marcador de cada minuto
def buscar_gol_minuto_a_minuto(partido):
    # pasos ← 0
    pasos = 0
    # PARA CADA minuto, del primero al último
    for minuto in range(len(partido)):
        # pasos ← pasos + 1
        pasos += 1
        # SI ya hay gol en ese minuto
        if partido[minuto] > 0:
            # DEVUELVE el minuto y los pasos
            return minuto, pasos
    # DEVUELVE -1: no hubo gol
    return -1, pasos


# El mismo partido del ep. 001: 90 minutos y el gol cae en el minuto 37 (Python cuenta desde el 0).
partido = [0] * 37 + [1] * 53


if __name__ == "__main__":
    minuto, pasos = buscar_gol_minuto_a_minuto(partido)
    print(f"gol en el 37 → minuto: {minuto}, pasos: {pasos}")

    assert buscar_gol_minuto_a_minuto(partido) == (37, 38)
    assert buscar_gol_minuto_a_minuto([0] * 89 + [1]) == (89, 90)
    assert buscar_gol_minuto_a_minuto([0] * 90) == (-1, 90)
    assert buscar_gol_minuto_a_minuto([1] * 90) == (0, 1)
    assert buscar_gol_minuto_a_minuto([]) == (-1, 0)
    print("Todos los casos pasan.")
