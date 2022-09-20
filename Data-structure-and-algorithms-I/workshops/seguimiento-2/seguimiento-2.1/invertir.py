from collections import deque
from linkedLists import *


def invertir(head: Node) -> Node:
    temp = head
    p = deque()
    while temp != None:
        p.append(temp.val)
        temp = temp.next
    list = None
    for i in range(len(p)):
        list = insertarAlFinal(list, p.pop())
    return list
    

def insertarAlFinal(head, val):
    if head is None:
        new = Node(val)
        return new
 
    if head.next is None:
        new = Node(val)
        head.next = new
        return head
     
    insertarAlFinal(head.next, val)
    return head


def main():
    # TEST NO. 1
    head1 = None
    head1 = insertAtEnd(head1, 1)
    head1 = insertAtEnd(head1, 2)
    head1 = insertAtEnd(head1, 3)
    head1 = insertAtEnd(head1, 4)
    head1 = insertAtEnd(head1, 5)

    printll(head1)
    print()
    head1 = invertir(head1)
    printll(head1)
    print()

    # TEST NO. 2
    head2 = None
    head2 = insertAtEnd(head2, 2)
    head2 = insertAtEnd(head2, 4)
    head2 = insertAtEnd(head2, 6)
    head2 = insertAtEnd(head2, 8)
    head2 = insertAtEnd(head2, 10)

    printll(head2)
    print()
    head2 = invertir(head2)
    printll(head2)
    print()


if __name__ == '__main__':
    main()