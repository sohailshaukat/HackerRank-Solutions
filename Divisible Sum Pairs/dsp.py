'''
Arguments: int(no of elements in list), int(divisor), list(elements)
Output: int(occurrence of sums that are divisible by divisor)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def divisibleSumPairs(n, k, ar):
    counter = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k == 0:
                counter += 1
    return counter
