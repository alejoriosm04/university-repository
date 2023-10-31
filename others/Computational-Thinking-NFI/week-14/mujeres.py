cantidadMujeres = int(input())
acumuladorMujeres = 0
i = 0

while(i < cantidadMujeres):
    salario = float(input())
    acumuladorMujeres += salario

print("Las mujeres de la empresa ganan en total " + str(acumuladorMujeres))