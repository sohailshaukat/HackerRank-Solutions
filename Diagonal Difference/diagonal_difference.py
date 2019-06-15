'''
Arguments:list(matrix)
Output: int(abs diff b/n the sums of the matrix's two diagonals)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def diagonalDifference(arr):
    first_diag = 0
    second_diag = 0
    n = len (arr)
    counter_first = 0
    counter_second = 0
    for i in range(0,n):
        first_diag += arr[i][i]
        second_diag += arr[i][n-i-1]
    return abs(first_diag-second_diag)
