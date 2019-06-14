'''
Arguments: int(no. of sequences), list(Queries)
Output: int(query result)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def dynamicArray(n, queries):
    big_sequence = [[] for _ in range(n)]
    la = 0
    la_arr = []
    for el in queries:
        q,x,y = el[0],el[1],el[2]
        index = ((x^la)%n)
        if q == 1:
            big_sequence[index].append(y)
        elif q == 2:
            size = len(big_sequence[index])
            la = big_sequence[index][y%size]
            la_arr.append(la)
    return la_arr
