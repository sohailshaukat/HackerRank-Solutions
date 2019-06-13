'''
Arguments: node(head of the linked list), data(to be inserted as a new node), int(position at which new node is to be inserted)
Output: node(head of new linked list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def insertNodeAtPosition(head, data, position):
    current = head
    position-=1
    Node = SinglyLinkedListNode(data)
    while position:
        current = current.next
        position-=1
    temp = current.next
    current.next = Node
    Node.next = temp
    return head
