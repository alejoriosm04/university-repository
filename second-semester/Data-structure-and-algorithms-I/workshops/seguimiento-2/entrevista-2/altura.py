class Node:
    def __init__(self, val=0, left=None,mid=None, right=None):
        self.val = val
        self.left = left
        self.mid = mid
        self.right = right


def Altura(root: Node):
    # Tree is totally empty
    if root is None:
        return 0
    
    # Return the actual Node, when it gets to a depth leave of the tree or is a root with only 1 Node
    if root.right is None and root.left is None and root.mid is None:
        return 1

    # Go to the right node, left and mid are NULL and return the max value of one of these
    # Also sum the actual node + 1
    if root.right is None:
        return max(Altura(root.left), Altura(root.mid)) + 1

    # Go to the left node, right and mid are NULL and return the max value of one of these
    # Also sum the actual node + 1
    if root.left is None:
        return max(Altura(root.right), Altura(root.mid)) + 1

    # Go to the mid node, left and right are NULL and return the max value of one of these
    # Also sum the actual node + 1
    if root.mid is None:
        return max(Altura(root.right), Altura(root.left)) + 1

    # Go through mid Node, right and left are NULL
    # Sum actual node + 1
    if root.right is None and root.left is None:
        return Altura(root.mid) + 1

    # Go through left Node, right and mid are NULL
    # Sum actual node + 1
    if root.left is None and root.mid is None:
        return Altura(root.right) + 1

    # Go through right Node, mid and left are NULL
    # Sum actual node + 1
    if root.right is None and root.mid is None:
        return Altura(root.left) + 1

    # Any nodes are NULL, return the max value going through all the branches (right, left and mid)
    else:
        return max(Altura(root.right), Altura(root.left), Altura(root.mid)) + 1


def main():
    pass


if __name__ == '__main__':
    main()