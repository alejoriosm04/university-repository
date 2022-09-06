from linkedLists import *


def invertir(head: Node):
    if head == None:
        return head
    else:
        anterior = None
        actual = head
        siguiente = actual.next
        while actual != None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente
        head = anterior
        return head


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)
    printll(head)

    head = invertir(head)
    printll(head)


if __name__ == '__main__':
    main()