#! python3
'''
problem URL: https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
Input Format:
    3
    2 3
    -1 -1
    -1 -1
    2
    1
    1
'''

import os
import sys


class Node:

    def __init__(self, info, left=None, right=None, depth=0):
        self.info = info
        self.left = left
        self.right = right
        self.depth = depth


def makeTree(indexes):
    '''
    Takes in a list of indexes, and returns the heap made out of the tree.
    Indexes will come in the format:
        [[ 2, 3],[ -1, -1],[ -1, -1]]
    Tree representation of this would be:
              1
             / \
            2   3
            p.s. -1 represents No child (None).
    The resultant-heap would be:
        [1, 2, 3] 
    '''
    root = Node(1, depth=1)
    stack = [root]
    sptr = 0
    ptr = 0
    while ptr < len(indexes):
        dpth = stack[sptr].depth
        if indexes[ptr][0] != -1:
            node = Node(indexes[ptr][0], depth=dpth+1)
            stack[sptr].left = node
            stack.append(node)
        if indexes[ptr][1] != -1:
            node = Node(indexes[ptr][1], depth=dpth+1)
            stack[sptr].right = node
            stack.append(node)
        sptr += 1
        ptr += 1
    return stack


def inOrder(root):
    '''
    This is a recursive function that takes in root of the tree as argument and returns a list of nodes enlisted inOrder. 
    [L-D-R] 
    For More about InOrder Traversal : https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    '''
    nodes = []
    if root:
        nodes.extend(inOrder(root.left))
        nodes.append(root.info)
        nodes.extend(inOrder(root.right))
    return nodes


def swapNodes(indexes, queries):
    '''
    Takes in indexes and queries as arguments.
    Indexes will contain a tree in below format:
        [[ 2, 3],[ -1, -1],[ -1, -1]]
    Tree representation of this would be:
              1
             / \
            2   3
            p.s. -1 represents No child (None).
    Queries will contain list of query, each query is at amount of steps the tree is meant to swapped.
        If a query = 2,
            nodes at depth 2,4,6,8 will have their child nodes swapped.
    '''
    sys.setrecursionlimit(10000000)
    results = []
    stack = makeTree(indexes)
    for query in queries:
        sptr = 0
        while sptr < len(stack):
            if stack[sptr].depth % query == 0:
                stack[sptr].left, stack[sptr].right = stack[sptr].right, stack[sptr].left
            sptr += 1
        results.append(inOrder(stack[0]))
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
