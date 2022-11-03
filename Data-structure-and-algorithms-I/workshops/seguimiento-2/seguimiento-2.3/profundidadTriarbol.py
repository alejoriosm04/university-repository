class Node:
    def __init__(self, val=0, left=None, right=None, middle=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right


def depth(root):
    if root == None:
        return 0
    if root.right == None and root.middle == None and root.left == None:
        return 1
    if root.left == None and root.middle == None:
        return depth(root.right) + 1
    if root.left == None and root.right == None:
        return depth(root.middle) + 1
    if root.right == None and root.middle == None:
        return depth(root.left) + 1
    if root.left == None:
        return depth(root.middle) + depth(root.right) + 1
    if root.right == None:
        return depth(root.middle) + depth(root.left) + 1
    if root.middle == None:
        return depth(root.left) + depth(root.right) + 1
    else:
        return depth(root.left) + depth(root.right) + depth(root.middle) + 1


def depth_height(root):
    if root == None:
        return 0
    if root.right == None and root.middle == None and root.left == None:
        return 1
    if root.left == None and root.middle == None:
        return depth_height(root.right) + 1
    if root.left == None and root.right == None:
        return depth_height(root.middle) + 1
    if root.right == None and root.middle == None:
        return depth_height(root.left) + 1
    if root.left == None:
        return max(depth_height(root.right), depth_height(root.middle)) + 1
    if root.right == None:
        return max(depth_height(root.left), depth_height(root.middle)) + 1
    if root.middle == None:
        return max(depth_height(root.right), depth_height(root.left)) + 1
    else:
        return max(depth_height(root.right), depth_height(root.middle), depth_height(root.left)) + 1


def main():
    n4 = Node(4, Node(10))
    n5 = Node(5)
    n6 = Node(6)
    n8 = Node(8)
    n7 = Node(7)
    n9 = Node(9)

    n2 = Node(2, n4, n5, n6)
    n3 = Node(3, n7, n8, n9)
    n1 = Node(1)

    n0 = Node(0, n1, n2, n3)

    print(depth(n0))
    print(depth_height(n0))


if __name__ == '__main__':
    main()