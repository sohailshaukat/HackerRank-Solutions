'''
problem URL: https://www.hackerrank.com/challenges/capitalize/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def solve(s):
    words = s.split(' ')
    words = [word.capitalize() for word in words]
    return(' '.join(words))
