def plantavieja(arreglo: list)->str:
    maximo = 0
    for diccionario in arreglo:
        if maximo < diccionario["antiguedad"]:
            maximo = diccionario["antiguedad"]
            nombre = diccionario["nombre"]
    return nombre