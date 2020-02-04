#! python3
'''
problem URL: https://www.hackerrank.com/challenges/find-the-nearest-clone/copy-from/140933385?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''


class Node:

    def __init__(self):
        self.colorcode = None
        self.neighbors = set()


def connect(nodeA, nodeB):

    nodeA.neighbors.add(nodeB)
    nodeB.neighbors.add(nodeA)


[node_count, edge_count] = list(map(int, input().rstrip().split()))

nodes = [Node() for _ in iter(range(node_count))]

for _ in iter(range(edge_count)):

    [nodeA, nodeB] = list(map(int, input().rstrip().split()))

    connect(nodes[nodeA-1], nodes[nodeB-1])

colors = list(map(int, input().rstrip().split()))

target = int(input().rstrip())

locations = []
ptr = 0
for splash in zip(nodes, colors):

    if splash[1] == target:
        locations.append(ptr)
    splash[0].colorcode = splash[1]

    ptr += 1


def getColor(node): return node.colorcode


def findShortestPath(nodeA, nodeB):
    queue = [nodeA]
    level = [0]
    ptr = 0

    while ptr < len(queue):
        prev_level = level[ptr]
        for node in queue[ptr].neighbors:
            if node == nodeB:
                return prev_level + 1
            elif node not in queue:
                queue.append(node)
                level.append(prev_level+1)
        ptr += 1

    return 0


paths = []
minimum = 999999999
for A in iter(locations[:-1]):
    for B in iter(locations[1:]):
        path = findShortestPath(nodes[A], nodes[B])
        if path > 0 and path < minimum:
            minimum = path

if minimum == 999999999:
    print(-1)
else:
    print(minimum)
