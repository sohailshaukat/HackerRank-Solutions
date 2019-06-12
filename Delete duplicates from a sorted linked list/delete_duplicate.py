'''
Arguments: node(head of Linked List)
Output: node(head of new linked list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def removeDuplicates(head):
    stack = []
    current = head
    while current:
        stack.append(current.data)
        current = current.next
    stack = list(set(stack))
    nlist = SinglyLinkedList()
    for el in stack:
        nlist.insert_node(el)
    return nlist.head
