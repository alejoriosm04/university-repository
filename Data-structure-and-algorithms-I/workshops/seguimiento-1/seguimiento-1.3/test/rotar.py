from linkedLists import *


def rotar(head: Node, k):
    if head == None:
        return head
    
    longitud = 1
    temp = head

    while temp.next:
        temp = temp.next
        longitud += 1

    k = k % longitud

    if k == 0:
        return head

    actual = head
    for i in range(longitud - k - 1):
        actual = actual.next
    
    nueva_cabeza = actual.next
    actual.next = None
    temp.next = head

    return nueva_cabeza


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    head = rotar(head, 38)

    printll(head)


if __name__ == '__main__':
    main()