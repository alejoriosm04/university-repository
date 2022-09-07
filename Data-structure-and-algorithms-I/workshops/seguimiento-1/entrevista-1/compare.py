from linkedLists import *


def compare(l1 : Node, l2 : Node):
    equal = True
    if l1 == None:
        return False
    else:
        while l1 != None:
            if l1.val != l2.val:
                equal = False
                break
            l1 = l1.next
            l2 = l2.next
        return equal


# def largo(head):
#     if head == None:
#         return 0
#     else:
#         return 1 + largo(head.next)
# def compare(l1: Node, l2: Node) -> bool:
#     largo1= largo(l1)
#     largo2 = largo(l2)
#     if largo1!=largo2:
#         return False
#     else:
#         for i in range(largo1):
#             if l1.val!=l2.val:
#                 return False
#                 break
#             else:
#                 l1 = l1.next
#                 l2 = l2.next


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

    head2 = None
    head2 = insertAtEnd(head2, 1)
    head2 = insertAtEnd(head2, 2)
    head2 = insertAtEnd(head2, 3)
    head2 = insertAtEnd(head2, 4)
    head2 = insertAtEnd(head2, 5)

    printll(head2)
    print()

    print(compare(head1, head2))

    # TEST NO. 2
    head3 = None
    head3 = insertAtEnd(head3, 1)
    head3 = insertAtEnd(head3, 2)
    head3 = insertAtEnd(head3, 3)
    head3 = insertAtEnd(head3, 4)
    head3 = insertAtEnd(head3, 5)

    printll(head3)
    print()

    head4 = None
    head4 = insertAtEnd(head4, 1)
    head4 = insertAtEnd(head4, 2)
    head4 = insertAtEnd(head4, 3)
    head4 = insertAtEnd(head4, 7)
    head4 = insertAtEnd(head4, 5)

    printll(head4)
    print()

    print(compare(head3, head4))


if __name__ == '__main__':
    main()