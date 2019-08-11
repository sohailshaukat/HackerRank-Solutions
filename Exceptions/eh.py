'''
problem URL: https://www.hackerrank.com/challenges/exceptions/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
t = int(input())
for _ in range(t):
    [a,b] = input().split()
    try:
        a = int(a)
        b = int(b)
        print(a//b)
    except ValueError as v :
        print("Error Code:",v)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
