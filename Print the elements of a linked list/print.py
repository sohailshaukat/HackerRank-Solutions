'''
Arguments: node(head of linked list)
Output: data(linked list data)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next
