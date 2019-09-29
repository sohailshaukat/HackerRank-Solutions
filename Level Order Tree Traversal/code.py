#! python3
'''
problem URL: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def levelOrder(root):
    #Write your code here
    stack = [root]
    while stack:
        node = stack.pop(0)
        print(node.info, end=' ')
        if node.left: stack.append(node.left)
        if node.right:stack.append(node.right)