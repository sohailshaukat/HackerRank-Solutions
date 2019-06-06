'''
Arguments: list(keyboards), list(drives), int(balance)
Output: int(maximum spendable)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    least = min(keyboards) + min(drives)
    if least > b:
        return -1
    else:
        stack = []
        for el in keyboards:
            for ek in drives:
                if el+ek <= b:
                    stack.append(el+ek)
    return (max(stack))
