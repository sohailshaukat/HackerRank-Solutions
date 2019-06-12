'''
Arguments: root(tree)
Output: info of nodes traversed postorder
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def postOrder(root):
    #Write your code here
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end= ' ')
