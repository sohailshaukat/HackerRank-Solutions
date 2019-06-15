'''
Arguments: str(Single string s), int(n)
Output: int(a's occurence)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def repeatedString(s, n):
    rep = n / len(s)
    rem = n % len(s)
    rep = int(rep)
    new_str = s[0:rem]
    counter = 0
    for el in s:
        if el == 'a':
            counter += 1
    counter *= rep
    for el in new_str:
        if el == 'a':
            counter += 1
    return counter
