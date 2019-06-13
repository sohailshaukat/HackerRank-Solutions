'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def getHeight(self,root):
        #Write your code here
        current = root
        if current == None:
            return -1
        else:
            current_height = max(self.getHeight(root = current.left) , self.getHeight(root  = current.right)) + 1
        return current_height
