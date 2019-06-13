'''
Arguments: node(head of linked list A),node(head of linked list B)
Output: int(1 OR 0 if equal or not equal respectively)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def stacker(llist):
    current = llist
    stack = []
    while current:
        stack.append(current.data)
        current = current.next
    return stack
def compare_lists(llist1, llist2):
    stack1 = stacker(llist1)
    stack2 = stacker(llist2)
    if stack1 == stack2:
        return 1
    else:
        return 0
