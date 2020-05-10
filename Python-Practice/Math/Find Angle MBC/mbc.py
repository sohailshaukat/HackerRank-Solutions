'''
problem URL: https://www.hackerrank.com/challenges/find-angle/problem?h_r=internal-search
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import math
ab = int(input())
bc = int(input())
mbc = round(math.degrees(math.atan(ab/bc)))
print(str(mbc)+'°', end  = '')
