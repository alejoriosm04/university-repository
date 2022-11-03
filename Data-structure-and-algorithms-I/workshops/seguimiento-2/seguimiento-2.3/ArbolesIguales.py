class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ArbolesIguales(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 and root2:
        if root1.val == root2.val:
            return ArbolesIguales(root1.left, root2.left) and ArbolesIguales(root1.right, root2.right)
    else:
        return False