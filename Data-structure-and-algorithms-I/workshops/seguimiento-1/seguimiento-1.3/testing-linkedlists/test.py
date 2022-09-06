from LinkedList import node
from LinkedList import linkedList


def insertar(head: node, valor, posI):
    temp = node(valor)
    actual = head
    i = 1
    if posI == 1 or head == None:
        temp.next = head
        head = temp;
    else:
        while(i > -1):
            posI -= 1
            if actual.next == None:
                break
            if posI == 1:
                temp.next = actual.next
                actual.next = temp
                break
            if posI == 0:
                temp.next = None
                actual.next = temp
                break
            actual = actual.next
    return head

def main():
    ll = linkedList()
    ll.madd(1,2,3,6,5,7,8)
    print(insertar(ll.head, 5, 1))
    print(ll.getData())

main()