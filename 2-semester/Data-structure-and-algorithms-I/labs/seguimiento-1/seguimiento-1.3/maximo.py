from linkedLists import *


def maximo(head: Node, i = 0) -> int:
    if head == None:
        return i
    else:
        if head.val >= i:
            i = head.val
    return maximo(head.next, i)


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    print(maximo(head))


if __name__ == '__main__':
    main()