def subconjuntos(cadena):
    subconjuntosAux(cadena, "")
    
def subconjuntosAux(cadena, respuesta):
    if len(cadena) == 0:
        print(respuesta)
    else:
        subconjuntosAux(cadena[1:], respuesta+cadena[0]) 
        subconjuntosAux(cadena[1:], respuesta)
        
subconjuntos(input())