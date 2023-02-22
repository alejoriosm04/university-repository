divisas = int(input())
accion = int(input())

if accion == 1:
    comprar = int(input())
    divisas = divisas + comprar
elif accion == 2:
    vender = int(input())
    divisas = divisas - vender
    
print(divisas)