'''
Arguments: list(alice's points), list(bob's points)
Output: int(alice's comparison score),int(bob's comparison score)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(0,3):
        if a[i]<b[i]:
            bob += 1
        elif a[i]>b[i]:
            alice += 1
    return alice,bob
