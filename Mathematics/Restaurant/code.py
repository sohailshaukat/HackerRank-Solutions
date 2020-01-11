#! python3
'''
problem URL: https://www.hackerrank.com/challenges/restaurant/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def gcd(a, b):

    if a == 0:
        return b

    return gcd(b%a, a)

if __name__ == "__main__":
    
    times = int(input())
    
    for _ in iter(range(times)):
        [a, b] = list(map(int, input().split()))
        l = gcd(a,b)
        print((a*b)//(l*l))