'''
Arguments: int(number of elements), list(elements)
Output: int(runnerup)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    i = 0
    while(i<len(arr)):
        if arr[i]==winner:
            del arr[i]
            i -= 1
        i+=1
    print(max(arr))
