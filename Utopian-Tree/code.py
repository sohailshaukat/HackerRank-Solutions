#! usr/bin/env python3

times = int(input())

while times:
    n = int(input())
    if n%2 == 0:
        print(2**((n//2)+1)-1)
    else:
        print(2**(((n+1)//2)+1)-2)
    times -= 1
