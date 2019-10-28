#! python3
'''
problem URL: https://www.hackerrank.com/challenges/tree-top-view/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
-explaination for this in github-description of file
'''


def topView(root):
    ptr = 0
    stack = [(root, 0, 0)]
    while ptr < len(stack):
        level = stack[ptr][1]
        distance = stack[ptr][2]
        try:
            if stack[ptr][0].left != None:
                stack.append((stack[ptr][0].left, level + 1, distance - 1))
        except:
            pass
        try:
            if stack[ptr][0].right != None:
                stack.append((stack[ptr][0].right, level + 1, distance + 1))
        except:
            pass
        ptr += 1
    distance_dict = {}
    tree = []
    for node in stack:
        try:
            if distance_dict[node[2]]:
                pass
        except:
            distance_dict[node[2]] = True
            tree.append((node[0], node[2]))
    min_distance = 9999
    max_distance = 0
    for node in tree:
        if node[1] < min_distance:
            min_distance = node[1]
        elif node[1] > max_distance:
            max_distance = node[1]
    for distance in range(min_distance, max_distance+1):
        for node in tree:
            if node[1] == distance:
                print(node[0].info, end=" ")
