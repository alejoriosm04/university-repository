from linkedLists import *


def insertar(head: Node, valor, posI):
    temp = Node(valor)
    actual = head
    if posI == 1:
        temp.next = head
        head = temp
        return head
    elif head == None:
        return head
    else:
        for i in range(1, posI-1):
            actual = actual.next
            if actual == None:
                return head
                break
        if actual.next == None:
            actual.next = temp
            temp.next = None
            return head
        else:
            temp.next = actual.next
            actual.next = temp
            return head


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    head = insertar(head, 10, 1)
    printll(head)


if __name__ == '__main__':
    main()