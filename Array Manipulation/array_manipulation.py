'''
Arguments: int(len of zero array), list( queries)
Output: int(maximum value in the list after all the operations)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def arrayManipulation(n, queries):
    zeroes = [0]*(n+1)
    maximum = 0
    x = 0
    for i,el in enumerate(queries):
        a = el[0]-1
        b = el[1]
        k = el[2]
        zeroes[a] += k
        zeroes[b] -= k
    for i,el in enumerate(zeroes):
        x += el
        zeroes[i] = x

    return max(zeroes)
