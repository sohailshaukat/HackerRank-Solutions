#! python3
'''
problem URL: https://www.hackerrank.com/challenges/reverse-game/problem?h_r=next-challenge&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen-challenge&h_v=zen
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#! python3

times = int(input())

for _ in iter(range(times)):
    [r, k] = list(map(int, input().split())) 
    fptr = r-1
    sptr = 0
    ptr = 0
    nl = []
    while ptr < r:
        if ptr%2 :
            nl.append(sptr)
            sptr += 1
        else:
            nl.append(fptr)
            fptr -= 1
        ptr += 1
    print(nl.index(k))

