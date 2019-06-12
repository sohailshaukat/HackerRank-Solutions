'''
Arguments: node(head of Linked List), int( Position X)
Output: data(node value at positon X)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def getNode(head, positionFromTail):
    stack = []
    current = head
    while current:
        stack.append(current.data)
        current = current.next
    positionFromTail = (positionFromTail +1) * (-1)
    return stack[positionFromTail]
