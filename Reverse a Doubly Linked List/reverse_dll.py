'''
Arguments: node(head of doubly linked list)
Output: node(head of the reversed doubly linked list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def reverse(head):
    current = head
    while current:
        current.next, current.prev, new_head = current.prev,current.next, current
        current = current.prev
    return new_head
