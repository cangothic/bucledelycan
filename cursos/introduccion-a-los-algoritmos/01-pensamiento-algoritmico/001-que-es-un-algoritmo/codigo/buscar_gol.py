def buscar_gol_minuto_a_minuto(partido):
    """Entrada: el marcador de cada minuto del partido (0 mientras no hay gol, 1 desde que cae).
    Salida: el primer minuto en que ya se ve el gol (-1 si no hubo) y cuántos minutos miraste."""
    pasos = 0
    for minuto in range(len(partido)):
        pasos += 1
        if partido[minuto] > 0:
            return minuto, pasos
    return -1, pasos


# Un partido de juguete: 90 minutos y el gol cae en el minuto 37 (Python cuenta desde el 0).
partido = [0] * 37 + [1] * 53


if __name__ == "__main__":
    casos = {
        "gol en el 37": partido,
        "gol en el 89": [0] * 89 + [1],
        "0-0, sin gol": [0] * 90,
        "gol en el 0": [1] * 90,
    }
    for nombre, marcador in casos.items():
        minuto, pasos = buscar_gol_minuto_a_minuto(marcador)
        print(f"{nombre} → minuto: {minuto}, pasos: {pasos}")

    assert buscar_gol_minuto_a_minuto(partido) == (37, 38)
    assert buscar_gol_minuto_a_minuto([0] * 89 + [1]) == (89, 90)
    assert buscar_gol_minuto_a_minuto([0] * 90) == (-1, 90)
    assert buscar_gol_minuto_a_minuto([1] * 90) == (0, 1)
    assert buscar_gol_minuto_a_minuto([]) == (-1, 0)
    print("Todos los casos pasan.")
