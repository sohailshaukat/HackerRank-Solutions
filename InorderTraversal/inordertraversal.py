'''
Arguments: root(tree)
Output: info of nodes traversed inorder
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
