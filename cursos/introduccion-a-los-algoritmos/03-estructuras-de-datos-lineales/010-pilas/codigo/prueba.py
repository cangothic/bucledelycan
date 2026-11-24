from editor import texto, escribir, deshacer_accion, rehacer_accion

for palabra in ["hola", "mundo", "cruel"]:
    escribir(palabra)
deshacer_accion()
print(" ".join(texto))  # hola mundo
rehacer_accion()
print(" ".join(texto))  # hola mundo cruel
deshacer_accion()
deshacer_accion()
print(" ".join(texto))  # hola
escribir("amigo")
rehacer_accion()  # rehacer quedó vacía: no pasa nada
print(" ".join(texto))  # hola amigo
for _ in range(5):
    deshacer_accion()  # las tres últimas no tienen qué sacar
