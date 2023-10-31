cantidadAtletas = int(input())
contadorAtletas = 0
i = 0

while(i < cantidadAtletas):
    vueltas = int(input())
    if(vueltas > 10):
        contadorAtletas += 1
    i += 1

print(contadorAtletas)