'''
Arguments: node(head of the linked list),int(position of node to be deleted)
Output: node(head of the new linked list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def deleteNode(head, position):
    current = head
    if position:
        while position-1:
            current = current.next
            position-=1
        if current.next.next:
            current.next = current.next.next
        else:
            current.next = None
    else:
        head = head.next
    return head
