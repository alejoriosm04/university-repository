listaLibrosLeidos = []
numLibrosLeidos = int(input())

i = 1
while(i <= numLibrosLeidos):
    nombreLibro = input()
    listaLibrosLeidos.append(nombreLibro)
    i = i + 1

print(listaLibrosLeidos)