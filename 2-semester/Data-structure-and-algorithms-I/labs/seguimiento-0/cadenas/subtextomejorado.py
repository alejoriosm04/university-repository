palabra = input()
posicion_inicial = int(input())
posicion_final = int(input())

if posicion_final > len(palabra):
    print("Error")
elif posicion_inicial > posicion_final:
    print("Error2")
else:
    print(palabra[posicion_inicial:posicion_final+1])