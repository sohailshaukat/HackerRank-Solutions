'''
problem URL: https://www.hackerrank.com/challenges/incorrect-regex/problem
-sohailshaukat  ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import re
for _ in range(int(input())):
    validity = True
    reg = input()
    try:
        reg = re.compile(reg)
    except re.error:
        validity = False
    print(validity)
