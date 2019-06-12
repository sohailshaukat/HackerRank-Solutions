'''
Arguments: list(A), list(B)
Output: int(factors of elements A and B b/n A and B
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#supporting
def isfactor(n,b):
    for el in b:
        if el%n is not 0:
            return False
    return True
def isfinalfactor(a,b):
    for i in b:
        if a%i is not 0:
            return False
    return True
#main function
def getTotalX(a, b):
    #
    # Write your code here.
    #
    ub = min(b)+1
    lb = max(a)
    factors = []
    final_factors = []
    for i in range(lb,ub):
        if isfactor(i,b):
            factors.append(i)
    for j in factors:
        if isfinalfactor(j,a):
            final_factors.append(j)
    return len(final_factors)
