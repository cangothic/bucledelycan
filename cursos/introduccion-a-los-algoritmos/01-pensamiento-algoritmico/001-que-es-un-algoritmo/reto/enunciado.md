# Reto — // ep. 001 · ¿Qué es un algoritmo? (y por qué ya usas muchos)

## Enunciado

Escribe los pasos para encontrar el gol en la grabación de un partido **partiéndola a la mitad**: saltas a un minuto, miras el marcador y sabes si el gol fue antes o después. Escríbelos como algoritmo:

- Cada paso dice exactamente qué hacer. Nada de «más o menos», «por ahí» ni «hasta que te parezca».
- Siempre termina, aunque el partido acabe 0-0.
- Tiene entrada (el marcador de cada minuto) y salida (el minuto del gol, o que no hubo gol).

Puedes escribirlo en español, paso por paso. Si te animas, prográmalo en Python con el partido de juguete de [codigo/buscar_gol.py](../codigo/buscar_gol.py) y cuenta los pasos.

## Ejemplos

Con un partido de 90 minutos:

| Partido | Minuto a minuto | Partiendo a la mitad |
| --- | --- | --- |
| gol en el minuto 37 | 38 pasos | ¿? |
| gol en el minuto 89 | 90 pasos | ¿? |
| 0-0, sin gol | 90 pasos | ¿? |

## Casos límite a considerar

- El partido acaba 0-0: ¿cómo sabe tu algoritmo que ya puede rendirse?
- El gol cae en el primer minuto o en el último.
- La grabación dura un solo minuto.
- La grabación está vacía.

## Pistas

<details>
<summary>Pista 1</summary>

Usa dos marcas: dónde empieza y dónde termina la parte de la grabación donde todavía puede estar el gol.

</details>

<details>
<summary>Pista 2</summary>

Si en el minuto que miras ya va 1-0, no sabes si el gol fue justo ahí o antes. Apunta ese minuto y sigue buscando hacia atrás.

</details>

La solución se explica al inicio del siguiente video y estará aquí, en solucion.py, cuando salga ese video.
