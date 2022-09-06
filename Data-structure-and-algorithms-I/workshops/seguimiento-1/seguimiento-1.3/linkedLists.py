# Python code to insert a node in a
# given Singly Linked List (recursively)
 
class Node:
 
    # Structure of the node.
    def __init__(self, val):
        self.val = val
        self.next = None
     
 
# Function to insert a node at
# first position in the given
# Linked List
def insertAtFirst(listHead, val):
    new = Node(val)
    new.next = listHead
    return new
# Time Complexity - O(1)
 
 
# Function to insert a node
# at the end of the given
# Linked List (recursively)
def insertAtEnd(listHead, val):
    if listHead is None:
        new = Node(val)
        return new
 
    if listHead.next is None:
        new = Node(val)
        listHead.next = new
        return listHead
     
    insertAtEnd(listHead.next, val)
    return listHead
# Time Complexity - O(n)
 
 
# Function to insert a node
# at a specific position in
# the given Linked List (recursively)
def insertInBetween(temp, val, pos):
 
    # if head is None and given position is greater than 0
    if temp is None and pos>0:
        return temp
 
    # if the node is to be added at first position
    if pos==0:
        new = Node(val)
        new.next = temp
        return new
     
    # if the node is to be added at second position
    if pos==1:
        new = Node(val)
        new.ext = temp.next
        temp.next = new
        return temp
    insertInBetween(temp.next, val, pos-1)
    return temp
# Time Complexity - O(i)
 
 
# Function to print the Linked List through Recursion
def printll(head):
    if head==None:
        return
    print(head.val, end='  ->  ')
    printll(head.next)
# Time Complexity - O(n)
# where n is the length of the linked list
 
 
# Driver code
if __name__=='__main__':
     pass
     # Here you can add your code to test all the functions
 
# This code was implemented and adapted by Alejandro Rios