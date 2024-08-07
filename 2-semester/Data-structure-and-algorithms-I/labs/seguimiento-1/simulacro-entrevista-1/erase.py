# class Node: # No cambiar esta clase
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# # A function that erase the middle node in a linked list
# def eraseMiddle(head):
#     if head is None:
#         return None
#     if head.next is None:
#         return None
#     if head.next.next is None:
#         return None
#     current = head
#     while current.next.next is not None:
#         current = current.next
#     current.next = current.next.next
#     return head


from linkedLists import *


def erase(head: Node) -> Node:
    counter = length(head)
    middle = counter // 2
    temp = head
    if head == None:
        return head
    else:
        while(middle > 1):
            middle -= 1
            head = head.next
        head.next = head.next.next
    return temp


def length(head: None):
    if head == None:
        return 0
    else:
        head = head.next
        counter = 1
        while head != None:
            counter += 1
            head = head.next
        return counter


def main():
    head1 = None
    head1 = insertAtEnd(head1, 1)
    head1 = insertAtEnd(head1, 2)
    head1 = insertAtEnd(head1, 3)
    head1 = insertAtEnd(head1, 4)
    head1 = insertAtEnd(head1, 5)

    printll(head1)
    print()
    head1 = erase(head1)
    printll(head1)

    print()

    head2 = None
    head2 = insertAtEnd(head2, 1)
    head2 = insertAtEnd(head2, 2)
    head2 = insertAtEnd(head2, 3)
    head2 = insertAtEnd(head2, 4)
    head2 = insertAtEnd(head2, 5)
    head2 = insertAtEnd(head2, 6)

    printll(head2)
    print()
    head2 = erase(head2)
    printll(head2)


if __name__ == '__main__':
    main()