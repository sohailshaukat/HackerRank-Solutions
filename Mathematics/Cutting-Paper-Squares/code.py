#! python3
'''
problem URL: https://www.hackerrank.com/challenges/p1-paper-cutting/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''

from functools import reduce
from operator import mul

print(reduce(mul, map(int, input().split()))-1)
