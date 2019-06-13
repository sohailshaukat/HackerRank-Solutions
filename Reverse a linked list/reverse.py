'''
Arguments: node(head of linked list)
Output: node(head of the reversed linked list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def reverse(head):
    current = head
    stack =[]
    while current:
        stack.append(current.data)
        current = current.next
    s = stack[::-1]
    nlist = SinglyLinkedList()
    for el in s:
        nlist.insert_node(el)
    return nlist.head
