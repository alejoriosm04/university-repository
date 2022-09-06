from linkedLists import *


def borrar(head: Node, pos):
    if pos == 1:
        return head.next
    elif head == None:
        return 0
    else:
        temp = borrar(head.next, pos-1)
        head.next = temp
        return head


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    head = borrar(head, 1)

    printll(head)


if __name__ == '__main__':
    main()