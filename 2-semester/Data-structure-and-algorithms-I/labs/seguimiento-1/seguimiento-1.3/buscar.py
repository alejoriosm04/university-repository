from linkedLists import *


def buscar(head: Node, k : int) -> int:
    if head == None:
        return -1
    #if no encontramos el valor en el nodo:
    if head.val != k:
        laPosicionDelSiguienteEnAdelante = buscar(head.next,k)
        if laPosicionDelSiguienteEnAdelante == -1:
            return -1
        else:
            return 1 + laPosicionDelSiguienteEnAdelante
    else: #lo encontramos
        return 0


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    print(buscar(head, 4))


if __name__ == '__main__':
    main()