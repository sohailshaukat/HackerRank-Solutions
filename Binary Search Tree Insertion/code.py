'''
problem URL: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?h_r=next-challenge&h_v=zen
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

    def insert(self, val):
        # Enter you code here.
        ptr = self.root
        if not ptr:
            ptr = Node(val)
            self.root = ptr
            return
        root = ptr
        prev = ()
        while ptr:
            if val > ptr.info:
                prev = (ptr, True)
                ptr = ptr.right
            else:
                prev = (ptr, False)
                ptr = ptr.left
        if prev[1]:
            prev[0].right = Node(val)
        else:
            prev[0].left = Node(val)
        self.root = root
        return


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
