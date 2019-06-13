'''
Arguments: node(head of the linked list), data(to be inserted as a node)
Output: node(head of new linked list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def insertNodeAtTail(head, data):
    Node = SinglyLinkedListNode(data)
    if head:
        node = head
        while node.next:
            node = node.next
        node.next = Node
    else:
        head = Node
    return head
