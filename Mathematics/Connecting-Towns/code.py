#!/bin/python3
'''
problem URL: https://www.hackerrank.com/challenges/connecting-towns/problem?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import operator
from functools import reduce

t = int(input())

for _ in iter(range(t)):
    __ = int(input())
    routes = list(map(int, input().rstrip().split()))
    print(reduce(operator.mul,routes)%1234567)
