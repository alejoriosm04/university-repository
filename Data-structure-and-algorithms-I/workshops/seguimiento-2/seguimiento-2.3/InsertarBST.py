from binary_tree import *


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def InsertarBST(root, val):
    if root == None:
        root = Node(val)
        return root
    tree = root
    while(True):
        if val < root.val:
            if root.left == None:
                root.left = Node(val)
                break
            else:
                root = root.left
        if val > root.val:
            if root.right == None:
                root.right = Node(val)
                break
            else:
                root = root.right
    return tree


def main():
    n4 = Node(2)
    n5 = Node(6)
    n7 = Node(8)

    n2 = Node(4,n4,n5)
    n3 = Node(6,None,n7)
    
    n1 = Node(5,n2,n3)

    printTree(n1)
    print(InsertarBST(n1,1))
    printTree(n1)


if __name__ == '__main__':
    main()