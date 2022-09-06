from linkedLists import *

class Node:
    def __init__(self, fecha,nombre):
        self.fecha = fecha
        self.nombre = nombre
        self.next = None


def ordenar(head:Node):
    if head == None or head.next == None:
        return head

    mitad = getMitad(head)
    siguienteMitad = mitad.next

    mitad.next = None

    izquierda = ordenar(head)
    derecha = ordenar(siguienteMitad)

    listaordenada = sortedMerge(izquierda, derecha)
    return listaordenada


def sortedMerge(izquierda, derecha):
    result = None

    if izquierda == None:
        return derecha
    elif derecha == None:
        return izquierda

    if izquierda.fecha <= derecha.fecha:
        result = izquierda
        result.next = sortedMerge(izquierda.next, derecha)
    elif (izquierda.fecha == derecha.fecha) and (izquierda.nombre < derecha.nombre):
        result = izquierda
        result.next = sortedMerge(izquierda.next, derecha)
    else:
        result = derecha
        result.next = sortedMerge(izquierda, derecha.next)

    return result


def getMitad(head: Node):
    if head == None:
        return head

    slow = head
    fast = head

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow


def printll(head):
    if head==None:
        return
    print(str(head.fecha) + ", " + head.nombre, end='  ->  ')
    printll(head.next)


def insertAtEnd(listHead, fecha, nombre):
    if listHead is None:
        new = Node(fecha, nombre)
        return new
 
    if listHead.next is None:
        new = Node(fecha, nombre)
        listHead.next = new
        return listHead
     
    insertAtEnd(listHead.next, fecha, nombre)
    return listHead


def main():
    head1 = None
    head1 = insertAtEnd(head1, 1980, "Encanto")
    head1 = insertAtEnd(head1, 1975, "Sueños de un paraiso")
    head1 = insertAtEnd(head1, 2000, "Nunca me olvides")

    printll(head1)
    print()
    head1 = ordenar(head1)
    printll(head1)

    print()

    head2 = None

    printll(head2)
    print()
    head2 = ordenar(head2)
    printll(head2)

    print()

    head3 = None
    head3 = insertAtEnd(head3, 2006, "La vereda del destino")
    head3 = insertAtEnd(head3, 2006, "El olvido que seremos")
    head3 = insertAtEnd(head3, 1980, "Encanto")

    printll(head3)
    print()
    head3 = ordenar(head3)
    printll(head3)


if __name__ == '__main__':
    main()


# Class Solution

# class Node:
#     def __init__(self, fecha,nombre):
#         self.fecha = fecha
#         self.nombre = nombre
#         self.next = None

# def ordenar(head:Node):
#     cantidad=0
#     curr=head
#     while curr!=None:
#         cantidad+=1
#         curr=curr.next
#     for i in range(cantidad):
#         curr=head
#         if curr==None or curr.next==None:
#             return curr
#         else:
#             bef=None
#             curr=head
#             aft=head.next
#             while aft!=None:
#                 if curr.fecha>aft.fecha or (curr.fecha==aft.fecha and curr.nombre>aft.nombre):
#                     if bef!=None:
#                         AftAux=aft.next
#                         bef.next=aft
#                         aft.next=curr
#                         curr.next=AftAux
#                     else:
#                         AftAux=aft.next
#                         head=aft
#                         aft.next=curr
#                         curr.next=AftAux
#                     bef=aft
#                     aft=curr.next
#                 else:
#                     bef=curr
#                     curr=aft
#                     aft=aft.next
#     return head