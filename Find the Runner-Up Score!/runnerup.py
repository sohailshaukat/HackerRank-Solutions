'''
Arguments: int(number of elements), list(elements)
Output: int(runnerup)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(set(map(int, input().split()))))
    print(arr[-2])
