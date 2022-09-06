from linkedLists import *


def invertir(head: Node) -> Node:
    if head == None:
        return head
    else:
        previous = None
        current = head
        next = current.next
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        head = previous

        return head


def main():
    # TEST #1
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 2)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 4)
    head = insertAtEnd(head, 5)

    head = invertir(head)
    printll(head)


if __name__ == '__main__':
    main()