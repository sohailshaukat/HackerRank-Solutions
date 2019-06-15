'''
Arguments: int(no, of steps), list(of steps)
Output: int(no. of valleys)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1

    return valley
