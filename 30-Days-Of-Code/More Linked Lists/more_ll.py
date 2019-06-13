'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def removeDuplicates(self,head):
            #Write your code here
        current = head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head
