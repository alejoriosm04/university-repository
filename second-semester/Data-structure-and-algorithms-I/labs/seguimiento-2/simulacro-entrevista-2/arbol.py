class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def InsertarBST(root, val):
    counter = 0
    if root == None:
        root = Node(val)
        print(counter)
        return root
    tree = root
    while(True):
        counter += 1
        if val < root.val:
            if root.left == None:
                root.left = Node(val)
                print(counter)
                break
            else: 
                root = root.left
                continue
        if val > root.val:
            if root.right == None:
                root.right = Node(val)
                print(counter)
                break
            else:
                root = root.right
                continue

    return tree


def main():
    n = int(input())
    numbers = input().split(" ")
    tree = None
    for i in range(len(numbers)):
        tree = InsertarBST(tree, numbers[i])


if __name__ == '__main__':
    main()