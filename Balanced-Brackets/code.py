#!python3

for _ in iter(range(int(input()))):
    brackets = list(input().rstrip())
    try:
        open_stack = []
        for bracket in brackets:
            if bracket in "{[(":
                open_stack.append(bracket)
            else:
                assert(abs(ord(open_stack.pop()) - ord(bracket)) <3)
        else:
            assert(not open_stack)
            print("YES")
    except:
        print("NO")