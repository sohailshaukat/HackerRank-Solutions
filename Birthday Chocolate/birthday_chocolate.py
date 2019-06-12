'''
Arguments: int(no. of squares in the chocolate bar), list(chocolate squares with numbers), int(ron's birthday ), int(ron's birthmonth)
Output: int(Total Ways)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def birthday(s, d, m):
    counter = 0
    for i,el in enumerate(s):
        summer = sum(s[i:i+m])
        if summer == d:
            counter += 1
    return counter
