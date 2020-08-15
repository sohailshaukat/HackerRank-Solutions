for _ in iter(range(int(input()))):
    string = list(input())
    prev = string.pop()
    total_changes = 0
    while string:
        tmp = string.pop()
        if prev == tmp:
            total_changes += 1
        prev = tmp
    print(total_changes)