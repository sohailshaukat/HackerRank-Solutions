'''
Arguments: root(tree)
Output: info of nodes traversed preorder
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def preOrder(root):
    if root:
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)
