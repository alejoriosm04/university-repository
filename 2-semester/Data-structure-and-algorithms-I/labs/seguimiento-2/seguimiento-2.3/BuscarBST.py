class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BuscarBST(root, val):
    if BuscarBSTAux(root, val):
        return "YES"
    else:
        return "NO"


# This solution does not use the logic of a BST.
# The function checks all the possible solutions.
def BuscarBSTAux(root,val):
    if root == None:
        return False
    if root.val == val:
        return True
    if root.left == None and root.right == None: 
        return False
    if root.left == None:
        return BuscarBSTAux(root.right, val)
    if root.right == None:
        return BuscarBSTAux(root.left, val)
    return BuscarBSTAux(root.left, val) or BuscarBSTAux(root.right, val)


# This solution use the logic of a BST
# Going through the Nodes comparing if is greater or lower than
# Unfortunately, it does not work for all the possible cases
# def BuscarBSTAux(root, val):
#     if root == None:
#         return False
#     if root.val == val:
#         return True
#     if root.left == None and root.right == None: 
#         return False
#     if root.left == None or val > root.left.val:
#         return BuscarBSTAux(root.right, val)
#     if root.right == None or val > root.right.val:
#         return BuscarBSTAux(root.right, val)
    

def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2,n4,n5)
    n3 = Node(3,n6,n7)
    
    n1 = Node(1,n2,n3)
    print(BuscarBST(n1,5))

if __name__ == '__main__':
    main()