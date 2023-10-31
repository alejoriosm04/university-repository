def contarSismos(sismos):
    contadorSismosFuertes = 0
    i = 0

    while(i < len(sismos)):
        if(sismos[i] > 6.0):
            contadorSismosFuertes += 1
        i += 1

    return contadorSismosFuertes