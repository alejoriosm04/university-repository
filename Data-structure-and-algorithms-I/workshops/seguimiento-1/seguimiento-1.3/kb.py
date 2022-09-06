from linkedLists import *


def broken():
    pass


def main():
    pass


if __name__ == '__main__':
    main()


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
# #devuelve nodo inicial
# def insertarInicio(nodo: Node, head: Node, copia: Node):
#     if nodo.next is None:
#         nodo.next= head
#     else: 
#         insertarInicio(nodo.next, head, copia)
#     return copia
# #devuelve nodo inicial
# def insertarFinal(nodo:Node, headTexto, copia: Node):
#     if headTexto.next is None:
#         headTexto.next= nodo
#     else:
#         insertarFinal(nodo, headTexto.next, copia)
#     return copia
# def convertirNodos(palabra: str, head:Node, copiaCabeza:Node, i=1):
#     if i>=len(palabra)-1:
#         return copiaCabeza
#     else: 
#             nuevoNodo = Node(palabra[i])
#             head.next = nuevoNodo
#             convertirNodos(palabra, head.next, i+1, copiaCabeza )
#   # primera parte  
# def broken(s: str): 
#     palabraInicio=""
#     texto=""
#     for letra in s:
#         if letra == '[':
#            flag = False
#            #creamos el primr nodo y usamos la funcion de convertir
#            nodoInicio = #mandar al inicio
#            palabraInicio=""
#         elif letra == "]":
#             flag= True
#             palabraEnlazada= Node(palabraInicio[0])
#             palabraEnlazada = convertirNodos(palabraInicio,palabraEnlazada,palabraEnlazada )
#             #convertir texto a nodos
#             textoEnlazado= Node(texto[0])
#             textoEnlazado = convertirNodos(texto, textoEnlazado, textoEnlazado )
#             #le vamos a mandar el texto que llevamos y la palabra a agregar
#             nodoInicio= insertarInicio(palabraEnlazada, textoEnlazado, textoEnlazado)
#             palabraInicio= 
#             ""
#             texto=""
#         elif flag is False:
#             palabraInicio+=letra
#         else:
#             texto+=letra
#         #la palabra ya esta lista si la flag=True
#         head= Node(palabraInicio[0])
#         head = convertirNodos(palabraInicio, head, head)
#     return head