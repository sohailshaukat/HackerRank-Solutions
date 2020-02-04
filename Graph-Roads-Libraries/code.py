#!python3
'''
problem URL: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''

class Node:

    def __init__(self,val):
        self.val = val
        self.neighbors = []
        self.isLit = False

    def __repr__(self):
        return "Node: "+str(self.val)+"\tNeighbors: "+str(len(self.neighbors))+"\tLibrary:"+str(self.isLit)

    def addLibrary(self):
        if self.isLit == False:
            self.isLit = True
            for neighbor in self.neighbors:
                neighbor.addLibrary()   
        else:
            return

def connect(nodeA, nodeB):
    nodeA.neighbors.append(nodeB)
    nodeB.neighbors.append(nodeA)


query_count = int(input())
for _ in iter(range(query_count)):
    [n, m, c_lib, c_road] = list(map(int, input().rstrip().split()))

    stack = [Node(val) for val in iter(range(1,n+1))]

    for __ in iter(range(m)):
        [a, b] = list(map(int, input().rstrip().split()))

        connect(stack[a-1], stack[b-1])

    if c_lib > c_road:
        lib_count = 0

        for node in stack:
            if node.isLit == False:
                node.addLibrary()
                lib_count += 1
        print(lib_count*c_lib+(n-lib_count)*c_road)
    else:
        print(n*c_lib)