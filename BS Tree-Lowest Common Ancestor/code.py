#! python3
'''
problem URL: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''


def lca(root, v1, v2):
    # Enter your code here
    lower_limit = min(v1, v2)
    upper_limit = max(v1, v2)
    current = root
    while not (lower_limit <= current.info <= upper_limit):
        if upper_limit < current.info:
            current = current.left
        else:
            current = current.right
    return current
