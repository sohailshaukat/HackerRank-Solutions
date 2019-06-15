'''
Arguments: int(height and width)
Output: pattern
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def staircase(n):
    for i in range(1,n+1):
        elements = '#'*i
        spaces = ' '*(n-i)
        print(f"{spaces}{elements}")

if __name__ == '__main__':
    n = int(input())
    staircase(n)
