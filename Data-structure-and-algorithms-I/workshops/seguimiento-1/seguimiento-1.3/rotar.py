from linkedLists import *


def rotar(head: Node, k):
    if head == None:
        return head
    else:
        for i in range(k):
            actual = head
            while actual.next != None:
                lastNode = actual
                actual = lastNode.next
            lastNode.next = None
            actual.next = head
            head = actual
        return head


def main():
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    head = rotar(head, 3)

    printll(head)


if __name__ == '__main__':
    main()