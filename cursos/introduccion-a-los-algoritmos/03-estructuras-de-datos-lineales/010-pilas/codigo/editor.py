texto = []      # el documento: una lista de palabras
deshacer = []   # pila de lo que se puede deshacer
rehacer = []    # pila de lo que se puede rehacer


def escribir(palabra):
    texto.append(palabra)
    deshacer.append(palabra)
    rehacer.clear()  # camino nuevo: lo de rehacer ya no sirve


def deshacer_accion():
    if deshacer:
        palabra = deshacer.pop()
        texto.pop()
        rehacer.append(palabra)
    else:
        print("no hay nada que deshacer")


def rehacer_accion():
    if rehacer:
        palabra = rehacer.pop()
        texto.append(palabra)
        deshacer.append(palabra)
