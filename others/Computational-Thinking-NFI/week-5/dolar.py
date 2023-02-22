dolares = float(input())

if dolares >= 200 and dolares <= 2000:
    cambio = dolares * 3900
    print("COP " + str(cambio))
else:
    print("No se puede realizar el cambio")