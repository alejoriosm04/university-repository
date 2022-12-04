from linkedLists import *


def insertarAlInicio(head: Node, valor: int) -> Node:
    # Crear nodo
    nuevoNodo = Node(valor)
    # El siguiente del nuevo nodo es la cabeza
    nuevoNodo.next = head
    # Retorno del nuevoNodo
    return head


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 99)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    head = insertarAlInicio(head, 1)
    printll(head)


if __name__ == '__main__':
    main()