'''
Arguments: node(head of linked list A), node(head of linked list B)
Output: node(head of new merged list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def mergeLists(head1, head2):
    current = head1
    stack = []
    while current.next:
        stack.append(current.data)
        current = current.next
    current.next = head2
    while current:
        stack.append(current.data)
        current = current.next
    stack = sorted(stack)
    nlist = SinglyLinkedList()
    for el in stack:
        nlist.insert_node(el)
    return nlist.head
