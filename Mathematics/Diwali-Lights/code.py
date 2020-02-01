#!pyhton3
'''
problem URL: https://www.hackerrank.com/challenges/diwali-lights/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''

times = int(input())

for _ in iter(range(times)):
    bulb_count = int(input())
    print((2**bulb_count -1)%100000)