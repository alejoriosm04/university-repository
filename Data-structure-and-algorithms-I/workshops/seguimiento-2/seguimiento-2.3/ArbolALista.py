from binaryTree import *


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ArbolALista(root: Node):
    if root is None or (root.left is None and root.right is None):
        return

    if root.left:
        ArbolALista(root.left)
        tmpRight = root.right
        root.right = root.left
        root.left = None

        tree = root.right

        while(tree.right):
            tree = tree.right

        tree.right = tmpRight

    ArbolALista(root.right)

    return root


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printTree(root)
    print("---------------------")

    root = ArbolALista(root)

    printTree(root)


if __name__ == '__main__':
    main()
