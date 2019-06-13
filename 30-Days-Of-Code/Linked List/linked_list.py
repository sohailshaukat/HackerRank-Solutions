'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
 def insert(self,head,data):
    #Complete this method
        node = Node(data)
        if head == None:
            head = node
        else:
            current = head
            while(current.next is not None):
                current = current.next
            current.next = node
        return head
