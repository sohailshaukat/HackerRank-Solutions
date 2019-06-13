'''
Arguments: node(head of the linked list), data(to be inserted as a new node)
Output: node(head of the new linked list)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def insertNodeAtHead(llist, data):
    # Write your code here
    Node = SinglyLinkedListNode(data)
    if llist:
        Node.next=llist
        return Node
    else:
        return Node
