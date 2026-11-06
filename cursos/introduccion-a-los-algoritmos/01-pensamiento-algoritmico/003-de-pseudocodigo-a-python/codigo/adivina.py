# elige un secreto al azar
import random
secreto = random.randint(1, 100)
# intentos ← 0 · intento ← ninguno
intentos = 0
intento = None
# MIENTRAS el intento no sea el secreto
while intento != secreto and intentos < 7:
    # pide un número y cuenta el intento
    intento = int(input("Tu número: "))
    intentos += 1
    # SI es menor, di «mayor»; SI es mayor, di «menor»
    if intento < secreto:
        print("mayor")
    elif intento > secreto:
        print("menor")
# al final: ¿acertaste o se acabaron los intentos?
if intento == secreto:
    print(f"Adivinaste en {intentos} intentos")
else:
    print(f"Se acabaron: era el {secreto}")
