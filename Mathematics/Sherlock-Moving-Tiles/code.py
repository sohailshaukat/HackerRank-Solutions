#! python3
'''
problem URL: https://www.hackerrank.com/challenges/summing-the-n-series/problem?h_r=next-challenge&h_v=zen
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
[l, s1, s2] = list(map(int, input().split()))

dl = abs(s2-s1)/(2**0.5)

qcount = int(input())

for _ in iter(range(qcount)):
    q = int(input())
    ql = q**0.5
    print((l-ql)/dl)
