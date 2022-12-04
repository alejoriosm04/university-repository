# Python code to insert a node in a
# given Singly Linked List (recursively)
 
class Node:
 
    # Structure of the node.
    def __init__(self, item):
        self.item = item
        self.nxt = None
     
 
# Function to insert a node at
# first position in the given
# Linked List
def insertAtFirst(listHead, item):
    new = Node(item)
    new.nxt = listHead
    return new
# Time Complexity - O(1)
 
 
# Function to insert a node
# at the end of the given
# Linked List (recursively)
def insertAtEnd(listHead, item):
    if listHead is None:
        new = Node(item)
        return new
 
    if listHead.nxt is None:
        new = Node(item)
        listHead.nxt = new
        return listHead
     
    insertAtEnd(listHead.nxt, item)
    return listHead
# Time Complexity - O(n)
 
 
# Function to insert a node
# at a specific position in
# the given Linked List (recursively)
# def insertInBetween(temp, item, pos):
 
#     # if head is None and given position is greater than 0
#     if temp is None and pos>0:
#         return temp
 
#     # if the node is to be added at first position
#     if pos==0:
#         new = Node(item)
#         new.nxt = temp
#         return new
     
#     # if the node is to be added at second position
#     if pos==1:
#         new = Node(item)
#         new.nxt = temp.nxt
#         temp.nxt = new
#         return temp
#     insertInBetween(temp.nxt, item, pos-1)
#     return temp
# # Time Complexity - O(i)

def insertar(head: Node, valor, posI):
    if head == None:
        return head
    elif posI == 1:
        newNode = Node(valor)
        newNode.nxt = head
        head = newNode
        return head
    elif posI == 2:
        if head.nxt == None:
            newNode = Node(valor)
            head.nxt = newNode
            newNode.nxt = None
            return head
        else:
            newNode = Node(valor)
            newNode.nxt = head.nxt
            head.nxt = newNode
            return head
    insertar(head.nxt, valor, posI-1)
    return head
 
 
# Function to print the Linked List through Recursion
def printll(head):
    if head==None:
        return
    print(head.item, end=' ')
    printll(head.nxt)
# Time Complexity - O(n)
# where n is the length of the linked list
 
 
# Driver code
if __name__=='__main__':
     
    head = None
 
    # Creating a Linked List of length 15
    for i in range(1, 16):
        head = insertAtEnd(head, i)
     
    # Insert node with value 100
    # at 4th position
    head = insertar(head, 100, 3)
 
    # # Insert node with value 101
    # # at 200th position
    # head = insertInBetween(head, 101, 200)
 
    # # Insert node with value 100
    # # at 1st position
    # head = insertAtFirst(head, 100)
 
    # # Insert node with value 100
    # # at the end position
    # head = insertAtEnd(head, 100)
 
    # Printing the new linked list
    printll(head)
 
# This code is contributed by Harshit Rathore