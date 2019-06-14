'''
Arguments: list(numbers)
Output: tuple(minimum sum,  maximum sum)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def miniMaxSum(arr):
    arr = sorted(arr)
    min_sum = sum(arr[0:4])
    max_sum = sum(arr[1:])
    print(min_sum,max_sum)
