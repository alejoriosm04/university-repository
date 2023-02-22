nombre_del_candidato1 = input()
cantidad_votos1 = int(input())

nombre_del_candidato2 = input()
cantidad_votos2 = int(input())

if cantidad_votos1 > cantidad_votos2:
    print("El presidente electo es " + nombre_del_candidato1)
elif cantidad_votos2 > cantidad_votos1:
    print("El presidente electo es " + nombre_del_candidato2)
else:
    print("Hay empate")