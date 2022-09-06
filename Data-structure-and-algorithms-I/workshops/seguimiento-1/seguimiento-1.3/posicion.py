from linkedLists import *


def posicion(head: Node, i: int) -> int:
    if head == None:
        return 0
    else:
        if i == 1:
            return head.val
        else:
            return posicion(head.next, i-1)


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    print(posicion(head, 1))


if __name__ == '__main__':
    main()