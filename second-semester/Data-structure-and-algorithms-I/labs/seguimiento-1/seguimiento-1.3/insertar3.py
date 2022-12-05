from linkedLists import *


# Solution
def insertar(head: Node, valor, posI):
    if head == None:
        return head
    elif posI == 1:
        newNode = Node(valor)
        newNode.next = head
        head = newNode
        return head
    elif posI == 2:
        if head.next == None:
            newNode = Node(valor)
            head.next = newNode
            newNode.next = None
            return head
        else:
            newNode = Node(valor)
            newNode.next = head.next
            head.next = newNode
            return head
    insertar(head.next, valor, posI-1)
    return head
# Time Complexity - O(n)

def main():
    head = None
    head = insertAtEnd(head, 85)
    head = insertAtEnd(head, 8)
    head = insertAtEnd(head, 74)
    head = insertAtEnd(head, 100)

    head = insertar(head, 45, 2)
    printll(head)

if __name__ == '__main__':
    main()