class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.next = None


def insertarInicio(head, valor):
    if head is None:
        newHead = Nodo(valor)
        return newHead

    newHead = Nodo(valor)
    newHead.next = head
    head = newHead

    return head


def insertarFinal(head, valor):
    if head is None:
        newHead = Nodo(valor)
        return newHead

    if head.next is None:
        newHead = Nodo(valor)
        head.next = newHead
        return head

    insertarFinal(head.next, valor)

    return head


def insertarFinal2(head, valor):
    if head is None:
        newHead = Nodo(valor)
        return newHead
    else:
        head.next = insertarFinal2(head.next, valor)
        return head


def insertarPosI(head, valor, posI):
    if head is None and posI > 0:
        print("Ingrese una posicion valida")
        return head

    if head is None:
        newHead = Nodo(valor)
        return newHead
    
    elif posI == 1:
        newNodo = Nodo(valor)
        newNodo.next = head
        return newNodo
    elif posI == 2:
        newNodo = Nodo(valor)
        newNodo.next = head.next
        head.next = newNodo
        # temp = head.next
        # head.next = newNodo
        # newNodo.next = temp
        return head
    else:
        insertarPosI(head.next, valor, posI-1)

    return head


def invertirLista(head):
    if head is None:
        return head
    
    previo = None
    actual = head
    siguiente = actual.next

    while actual != None:
        siguiente = actual.next
        actual.next = previo
        previo = actual
        actual = siguiente

    head = previo
    return head


def printll(head):
    if head is None:
        return
    else:
        print(head.valor, end=' -> ')
        printll(head.next)


def main():
    head = None
    head = insertarFinal(head, 1)
    head = insertarFinal(head, 2)
    head = insertarFinal(head, 3)
    head = insertarFinal(head, 4)

    printll(head)
    print()

    head2 = None
    head2 = insertarFinal2(head2, 1)
    head2 = insertarFinal2(head2, 2)
    head2 = insertarFinal2(head2, 3)
    head2 = insertarFinal2(head2, 4)

    printll(head2)
    print()

    head3 = None
    head3 = insertarInicio(head3, 1)
    head3 = insertarInicio(head3, 2)
    head3 = insertarInicio(head3, 3)
    head3 = insertarInicio(head3, 4)

    printll(head3)
    print()

    head2 = insertarPosI(head2, 5, 3)
    printll(head2)
    print()

    head2 = invertirLista(head2)
    printll(head2)


if __name__ == '__main__':
    main()