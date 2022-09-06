# class Node: # No cambiar esta clase
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# # A function that checks if the linked list is a palindrome
# def isPalindrome(head):
#     if head is None:
#         return True
#     if head.next is None:
#         return True
#     if head.next.next is None:
#         return True
#     current = head
#     while current.next.next is not None:
#         current = current.next
#     current.next = current.next.next
#     return isPalindrome(head)

from linkedLists import *


def esPalindromo(head: Node) -> bool:
    esPalindromo = True
    head2 = invertir(head)

    if head == None:
        return False
    else:
        while head != None:
            if head.val != head2.val:
                esPalindromo = False
                break
            head = head.next
            head2 = head2.next
        return esPalindromo


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
    head = None
    head = insertAtEnd(head, 1)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 3)
    head = insertAtEnd(head, 1)
    printll(head)
    print()
    # printll(invertir(head))
    print()

    print(esPalindromo(head))
    print()

    head1 = None
    head1 = insertAtEnd(head1, 1)
    head1 = insertAtEnd(head1, 2)
    printll(head1)
    print()
    # printll(invertir(head1))
    print()

    print(esPalindromo(head1))
    print()
    printll(invertir(head1))


if __name__ == '__main__':
    main()