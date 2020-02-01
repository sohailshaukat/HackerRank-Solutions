#! python3
'''
problem URL: https://www.hackerrank.com/challenges/summing-the-n-series/problem?h_r=next-challenge&h_v=zen
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''

times = int(input())

for _ in iter(range(times)):
    n = int(input())
    print(int((n)*(1+(n-1)*1))%1000000007)