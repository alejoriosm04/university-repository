def contarCaninos(caninos):
    contadorMayor6 = 0
    i = 0

    while(i < len(caninos)):
        if(caninos[i]["edad"] >= 6.0):
            contadorMayor6 += 1
        i += 1

    return contadorMayor6