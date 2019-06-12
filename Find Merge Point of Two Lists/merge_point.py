'''
Arguments: node(head of linked list A),node(head of linked list B)
Output: data(data of the node that is the merge point of linked lists A and B)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def findMergeNode(head1, head2):
    current = head1
    stack = []
    while current:
        stack.append(current)
        current = current.next
    current = head2
    while current:
        if current.next in stack:
            return current.next.data
        current = current.next
    return
