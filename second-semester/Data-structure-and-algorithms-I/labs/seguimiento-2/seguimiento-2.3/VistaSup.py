from binaryTree import *
from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
def vistaSup(root):
    s = deque()
    if root == None:
        return ""

    tree = root
    while(root):
        s.append(root.val)
        if root.right:
            root = root.right
        else:
            break
    root = tree.left
    while(root):
        s.appendleft(root.val)
        if root.left:
            root = root.left
        else:
            break
    
    return list(s) # This should be a string but the program asks for a list, so... ._.


def main():
    n8 = Node(4)
    n4 = Node(3, None, n8)
    n7 = Node(6)
    n3 = Node(5, n4, n7)

    n2 = Node(2,None,n3)
    
    n1 = Node(1, None,n2)

    printTree(n1)
    print(vistaSup(n1))


if __name__ == '__main__':
    main()