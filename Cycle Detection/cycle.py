'''
Arguments: node (head of linked list)
Output: 0(if no cylce is found) OR 1(if cycle is found)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def has_cycle(head):
    stack = []
    current = head
    while current:
        if current.next in stack:
            return 1
        else:
            stack.append(current.next)
            current = current.next
    return 0
