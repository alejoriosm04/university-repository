class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def TamañoArbol(root):
    if root == None:
        return 0
    else:
        return 1 + TamañoArbol(root.left) + TamañoArbol(root.right)