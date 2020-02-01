#!python3
'''
problem URL: https://www.hackerrank.com/challenges/strange-grid/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''

[r, c] = list(map(int, input().split()))
r -= 1
c -= 1
level = r/2
tens = int(level)

if tens != level:
    units = 2*c + 1
else:
    units = 2*c

print(tens*10+units)
