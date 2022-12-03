from collections import deque
from linkedLists import *

## This functions did not work as expected
# class NodoDeLista:
#     """Nodo para construir una lista simplemente enlazada"""
#     def __init__(self, dato : int):
#         self.dato = dato
#         self.siguiente = None


# class NodoDeArbolTriario:
#     """Nodo para construir un árbol triario"""
#     def __init__(self, dato=0, izquierda=None, derecha=None, centro=None):
#         self.dato = dato
#         self.izquierda = izquierda
#         self.centro = centro
#         self.derecha = derecha

# def insert(root, item): 
#     temp = NodoDeLista(0) 
#     temp.dato = item 
#     temp.siguiente = root 
#     root = temp
#     return root


# def arrayToList(arr, n): 
#     root = None 
#     for i in range(n - 1, -1, -1): 
#         root = insert(root, arr[i])
#     return root


# def recorridoPorPisos(nodo : NodoDeArbolTriario) -> NodoDeLista:
#     lista = deque()
#     lista = recorridoPorPisosAux(nodo, lista)
#     n = len(lista)
#     root = arrayToList(lista, n)
#     return root


# def recorridoPorPisosAux(nodo : NodoDeArbolTriario, lista) -> NodoDeLista:
#     if nodo is None:
#         return lista
#     else:
#         lista.appendleft(nodo.dato)
#         recorridoPorPisosAux(nodo.derecha, lista)
#         recorridoPorPisosAux(nodo.centro, lista)
#         recorridoPorPisosAux(nodo.izquierda, lista)
#         return lista

class NodoDeLista:
    """Nodo para construir una lista simplemente enlazada"""
    def __init__(self, dato : int):
        self.dato = dato
        self.siguiente = None


class NodoDeArbolTriario:
    """Nodo para construir un árbol triario"""
    def __init__(self, dato=0, izquierda=None,centro=None, derecha=None):
        self.dato = dato
        self.izquierda = izquierda
        self.centro = centro
        self.derecha = derecha


def recorridoPorPisos(nodo):
    arreglo=[]
    incompleto=[nodo]
    if nodo==None:
        return None
    while(len(incompleto)!=0):
        control=incompleto.pop(0)
        arreglo.append(control)
        if control.izquierda!=None:
            incompleto.append(control.izquierda)
        if control.centro!=None:
            incompleto.append(control.centro)
        if control.derecha!=None:
            incompleto.append(control.derecha)
    cabeza=NodoDeLista(arreglo[-1].dato)
    retorno=cabeza
    Tamaño=len(arreglo)
    for i in range(Tamaño-1):
        retorno.siguiente=NodoDeLista(arreglo[Tamaño-2-i].dato)
        retorno=retorno.siguiente
    return cabeza


def main():
    n4 = NodoDeArbolTriario(4, NodoDeArbolTriario(10))
    n5 = NodoDeArbolTriario(5)
    n6 = NodoDeArbolTriario(6)
    n8 = NodoDeArbolTriario(8)
    n7 = NodoDeArbolTriario(7)
    n9 = NodoDeArbolTriario(9)

    n2 = NodoDeArbolTriario(2, n4, n5, n6)
    n3 = NodoDeArbolTriario(3, n7, n8, n9)
    n1 = NodoDeArbolTriario(1)

    n0 = NodoDeArbolTriario(0, n1, n2, n3)

    printll(recorridoPorPisos(n0))


if __name__ == '__main__':
    main()