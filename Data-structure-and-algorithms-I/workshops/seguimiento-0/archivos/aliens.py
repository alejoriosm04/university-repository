archivo = open("aliens.txt")
texto = archivo.read()
archivo.close()

lista_de_lineas = texto.splitlines()

nombre_ganador = ""
poder_ganador = 0

for linea in lista_de_lineas:
    nombre,poder_str = linea.split(",")
    poder = int(poder_str)
    
    if poder > poder_ganador:
        poder_ganador = poder
        nombre_ganador = nombre
    
print(nombre_ganador)