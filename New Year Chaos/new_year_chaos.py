#!/bin/python3
'''
Arguments:  list(queue final state)
Output: int(No. of bribes) or str(Too chaotic if one person bribes more than 2)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    arr = [k-1 for k in q]
    l = max(q)
    for i,p in enumerate(arr):
        if p - i > 2:
            print('Too chaotic')
            return
        for j in range(max(p-1 , 0),i): #this counts steps it took to come from behind 'p' = original actual index to the 'i' the rn index
            if arr[j] > p:
                moves += 1
    print( moves )




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
