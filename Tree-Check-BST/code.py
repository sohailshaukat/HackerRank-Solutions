#! python3
'''
problem URL: https://www.hackerrank.com/challenges/is-binary-search-tree/copy-from/131449870
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''


def check_bst(node, min_, max_):
    if node is None:
        return True
    if node.data < min_ or node.data > max_:
        return False
    return (check_bst(node.left, min_, node.data-1) and check_bst(node.right, node.data+1, max_))


def check_binary_search_tree_(root):
    return check_bst(root, -99999999, 99999999)
