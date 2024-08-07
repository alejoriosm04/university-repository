"""
Test the behavior of a binary tree
Written in Python by Alejandro Ríos
For the course "Data Structures and Algorithms I" at EAFIT University


   -  Links the functions and classes of binaryTree.py with your main file
   -  Prints your Binary Tree in the console
   -  Create a Binary Tree from scratch and see the output from your modifications

Clone the script binaryTree.py on your work folder (where your main file is).

This script is related to my linked list script: 
https://github.com/alejoriosm04/linked-list-script
Uploaded to GitHub Gist
""" 


# DONT CHANGE THIS CODE
# (UNLESS YOU NEED TO DO SPECIFIC MODIFICATIONS TO THE FUNCTIONS)


class Node:
    
    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val


# This function only works with BSTs
def insertBST(self, val):

    if self.val:
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
    else:
        self.val = val


# This function only works with BSTs   
def searchBST(self, val):
    if val < self.val:
        if self.left is None:
            return str(val) + " Not Found"
        return self.left.search(val)
    elif val > self.val:
        if self.right is None:
            return str(val) + " Not Found"
        return self.right.search(val)
    else:
        return str(self.val) + ' is found'


# Flatten a binary tree into linked list
def flatten(self):
    if self is None or (self.left is None and self.right is None):
        return

    if self.left:
        flatten(self.left)
        tmpRight = self.right
        self.right = self.left
        self.left = None

        tree = self.right

        while(tree.right):
            tree = tree.right

        tree.right = tmpRight

    flatten(self.right)

    return self


def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('  ' * 4 * level + "(" + str(level) + ")" + '-> ' + str(node.val))
        printTree(node.left, level + 1)


if __name__ == '__main__':
    pass


'''Implemented and adapted by Alejandro Ríos (GitHub: @alejoriosm04)'''
