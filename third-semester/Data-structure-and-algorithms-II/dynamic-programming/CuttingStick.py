def cortarVarilla(TamañoVarilla,listaPrecios):
    tabla= [0]*(TamañoVarilla+1)

    for Varilla_Actual in range (1,TamañoVarilla+1):
        mejor_valor=0
        
        print(tabla)
        for i in range (1,Varilla_Actual+1):
            valor=listaPrecios[i]+tabla[Varilla_Actual-i]#va buscar el precio de la varilla de longitud 2
            print(valor)
            if valor>mejor_valor:
                mejor_valor=valor
        tabla[Varilla_Actual]=mejor_valor
        print(tabla)

    return tabla [TamañoVarilla]
lista=[0,1,5,8,9,10]
cortarVarilla(4,lista)