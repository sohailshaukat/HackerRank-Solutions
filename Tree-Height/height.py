'''
Arguments: node(root node of the tree)
Output: int(height of the tree)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def height(root):
    current = root
    if current is None:
        return -1
    else:
        h = max(height(current.left), height(current.right)) + 1
    return h
