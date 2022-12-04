def nose(lista):
    lista = sorted(lista)
    contador = 0
    diccionario = {}
    diccionario2 = {}
    for i in range(len(lista)):
        diccionario[i] = lista[i]
    for i in range(min(diccionario.values()), max(diccionario.values())):
        if i not in diccionario.values() and i>0:
            diccionario2[i] = True
    if len(diccionario2)==0:
        print(max(list(diccionario.values()))+1)
    else:
        print(min(list(diccionario2.keys())))
        
        
lista = [-2,-1,1,3,4,5,6,7,8,9,10,11,12,13,20]
nose(lista)


def smallestMissing(arr):
    dict = {}
    for i in range(len(arr)):
        dict[arr[i]] = True
    
    number = 1
    while True:
        if number not in dict:
            return number
        number += 1

arr = [-2,-1,1,3,4,5,6,7,8,9,10,11,12,13,20]
smallestMissing(arr)