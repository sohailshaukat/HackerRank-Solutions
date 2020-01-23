#!pyhton3
'''
problem URL: https://www.hackerrank.com/challenges/sherlock-and-permutations/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''

from math import factorial

times = int(input())

for _ in iter(range(times)):

    [n, m] = list(map(int, input().split()))
    m -= 1
    r = n
    n = m+n
    p = factorial(n)//(factorial(r)*factorial(n-r))
    print(p%(10**9 + 7))
