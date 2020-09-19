def has_cycle(head):
    stack = []
    curr = head
    while curr:
        if curr not in stack:
            stack.append(curr)
        else:
            return True
        curr = head.next
    return False  