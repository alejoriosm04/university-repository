from linkedLists import *


def merge(head1, head2):
    head1 = mergeAux(head1, head2)
    return head1


def mergeAux(head1, head2):
    sorted = None
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    if head1.val <= head2.val:
        sorted = head1
        sorted.next = mergeAux(head1.next, head2)
    else:
        sorted = head2
        sorted.next = mergeAux(head1, head2.next)

    return sorted


def main():
    # TEST NO. 1
    head1 = None
    head1 = insertAtEnd(head1, 1)
    head1 = insertAtEnd(head1, 3)
    head1 = insertAtEnd(head1, 5)

    printll(head1)
    print()

    head2 = None
    head2 = insertAtEnd(head2, 2)
    head2 = insertAtEnd(head2, 4)
    head2 = insertAtEnd(head2, 6)

    printll(head2)
    print()

    printll(merge(head1, head2))


if __name__ == '__main__':
    main()