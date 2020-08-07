for _ in iter(range(int(input()))):
    
    string_1,string_2 = [set(input()) for __ in range(2)]
    
    if string_1 & string_2:
        print("YES")
    else:
        print("NO")