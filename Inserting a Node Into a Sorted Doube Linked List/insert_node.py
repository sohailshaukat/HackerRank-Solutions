def sortedInsert(head, data):
    current = head
    node = DoublyLinkedListNode(data)
    if current.data > data:
        node.next = current
        current.prev = node
        head = node
    else:
        while current.next:
            if current.data<= data < current.next.data:
                node.prev = current
                node.next = current.next
                current.next = node
                current.next.prev = node
                return head
            current = current.next
        current.next = node
        node.prev = current
    return head
