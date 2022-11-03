def SumaLista(lista):
    contador = 0
    for item in lista:
        contador = contador + item

    return contador


def MayorLista(lista):
    mayor = lista[0]
    for item in lista:
        if item > mayor:
            mayor = item

    return mayor


def PromedioLista(lista):
    numero_de_elementos = (len(lista))
    suma_elementos = 0
    for item in lista:
        suma_elementos = suma_elementos + item

    promedio = suma_elementos / numero_de_elementos

    return promedio


def main():
    lista_numeros = [10, 5, 8, 17]
    print(SumaLista(lista_numeros))
    print(MayorLista(lista_numeros))
    print(PromedioLista(lista_numeros))


main()