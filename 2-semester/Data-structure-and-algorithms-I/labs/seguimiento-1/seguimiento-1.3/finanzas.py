from linkedLists import *


def sumar(head1: Node, head2: Node):
    head1 = invertir(head1)
    head2 = invertir(head2)
    
    head1 = sumaAux(head1, head2)
    head1 = invertir(head1)

    # while head2.next != None:
    #     sum = int(head1.val) + int(head2.val)
    #     if sum >= 10:
    #         if head1.next != None:
    #             head1.val = sum-10
    #             head1.next.val += 1
    #         else:
    #             head1.val = sum-10
    #             head1.next = Node(1)
    #     else:
    #         head1.val = sum

    #     if head1.next == None:
    #         head1.next = head2.next
    #         break
    #     head1 = head1.next
    #     head2 = head2.next
    # Idk why this doesnt work ._.

    s = ""
    while head1 != None:
        s += str(head1.val)
        head1 = head1.next
    return s


def sumaAux(head1: Node, head2: Node):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    sum = head1.val + head2.val
    if sum >= 10:
        head1.val = sum - 10
        if head1.next != None:
            head1.next.val += 1
        else:
            head1.next = Node(1)
    else:
        head1.val = sum

    head1.next = sumaAux(head1.next, head2.next)
    return head1


def invertir(head: Node):
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
    head1 = None
    head1 = insertAtEnd(head1, 3)
    head1 = insertAtEnd(head1, 4)
    head1 = insertAtEnd(head1, 2)
    printll(head1)

    print()

    head2 = None
    head2 = insertAtEnd(head2, 4)
    head2 = insertAtEnd(head2, 6)
    head2 = insertAtEnd(head2, 5)

    printll(head2)

    print()

    print(sumar(head1, head2))

    head3 = None
    head3 = insertAtEnd(head3, 2)
    head3 = insertAtEnd(head3, 9)
    head3 = insertAtEnd(head3, 0)
    head3 = insertAtEnd(head3, 0)
    head3 = insertAtEnd(head3, 0)
    head3 = insertAtEnd(head3, 0)
    head3 = insertAtEnd(head3, 0)
    printll(head3)

    print()

    head4 = None
    head4 = insertAtEnd(head4, 3)
    head4 = insertAtEnd(head4, 1)
    head4 = insertAtEnd(head4, 0)
    head4 = insertAtEnd(head4, 0)
    head4 = insertAtEnd(head4, 0)
    head4 = insertAtEnd(head4, 0)
    head4 = insertAtEnd(head4, 0)

    printll(head4)

    print()

    print(sumar(head3, head4))

    head5 = None
    printll(head5)

    print()

    head6 = None
    printll(head6)

    print()

    print(sumar(head5, head6))


if __name__ == '__main__':
    main()