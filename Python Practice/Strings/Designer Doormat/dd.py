'''
problem URL: https://www.hackerrank.com/challenges/designer-door-mat/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import math
row = int(input().split()[0])
patt = '.|.'
for i in range(1,row+1):
    if i <= math.floor(row/2):
        print((patt*(2*(i-1)+1)).center(row*3,'-'))
    elif i == math.ceil(row/2):
        print('WELCOME'.center(row*3,'-'))
    else:
        print((patt*(2*(row-i)+1)).center(row*3,'-'))
