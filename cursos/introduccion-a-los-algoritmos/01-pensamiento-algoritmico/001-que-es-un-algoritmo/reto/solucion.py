"""Solución del reto — // ep. 001 · ¿Qué es un algoritmo? (y por qué ya usas muchos)

Los pasos precisos para encontrar el gol partiendo la grabación a la mitad:

1. Marca el primer minuto como «inicio» y el último como «fin». Todavía no has visto el gol.
2. Mientras «inicio» no haya pasado a «fin»:
   a. Salta al minuto que está justo en medio de «inicio» y «fin» y mira el marcador.
   b. Si ya va 1-0, el gol fue en ese minuto o antes: apúntalo y el nuevo «fin» es el minuto anterior.
   c. Si sigue 0-0, el gol fue después: el nuevo «inicio» es el minuto siguiente.
3. Cuando «inicio» pasa a «fin», el último minuto que apuntaste es el del gol.
   Si no apuntaste ninguno, el partido acabó 0-0.

Cada paso dice exactamente qué hacer, y el algoritmo siempre termina:
en cada vuelta la parte que te queda por ver se achica por lo menos a la mitad.
Funciona porque el marcador solo cambia en un sentido: 0-0 hasta el gol, 1-0 desde el gol.
Lo vamos a ver a fondo en el ep. 015 (búsqueda binaria).
"""
import os
import sys

# Para comparar con el algoritmo del video.
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "codigo"))
from buscar_gol import buscar_gol_minuto_a_minuto, partido  # noqa: E402


def buscar_gol_partiendo_a_la_mitad(partido):
    """Entrada: el marcador de cada minuto (0 hasta el gol, 1 desde el gol).
    Salida: el primer minuto con el gol (-1 si no hubo) y cuántos minutos miraste."""
    inicio, fin = 0, len(partido) - 1
    pasos = 0
    gol = -1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        pasos += 1
        if partido[medio] > 0:      # ya va 1-0: el gol fue aquí o antes
            gol = medio
            fin = medio - 1
        else:                       # sigue 0-0: el gol fue después
            inicio = medio + 1
    return gol, pasos


if __name__ == "__main__":
    casos = {
        "gol en el 37": partido,
        "gol en el 89": [0] * 89 + [1],
        "0-0, sin gol": [0] * 90,
        "gol en el 0": [1] * 90,
    }
    for nombre, marcador in casos.items():
        _, lento = buscar_gol_minuto_a_minuto(marcador)
        minuto, rapido = buscar_gol_partiendo_a_la_mitad(marcador)
        print(f"{nombre}: minuto {minuto} · minuto a minuto {lento} pasos · a la mitad {rapido} pasos")

    # Encuentra el gol en cualquier minuto de los 90.
    for g in range(90):
        assert buscar_gol_partiendo_a_la_mitad([0] * g + [1] * (90 - g))[0] == g
    # Casos límite: sin gol, partido vacío, un solo minuto.
    assert buscar_gol_partiendo_a_la_mitad([0] * 90)[0] == -1
    assert buscar_gol_partiendo_a_la_mitad([]) == (-1, 0)
    assert buscar_gol_partiendo_a_la_mitad([1]) == (0, 1)
    assert buscar_gol_partiendo_a_la_mitad([0]) == (-1, 1)
    # El del video: 7 vistazos. Y nunca más de 7 con 90 minutos (2⁷ = 128).
    assert buscar_gol_partiendo_a_la_mitad(partido) == (37, 7)
    assert max(buscar_gol_partiendo_a_la_mitad([0] * g + [1] * (90 - g))[1] for g in range(91)) <= 7
    print("Todos los casos pasan.")
