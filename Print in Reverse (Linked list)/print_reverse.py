'''
Arguments: node(head of linked list)
Output: data(in reverse order)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def reversePrint(head):
    current = head
    stack = []
    while current:
        stack.append(current.data)
        current = current.next
    while stack:
        x = stack.pop()
        print(x)
