'''
Arguments: list(clouds 0 being normal 1 being thunder cloud)
Output: int(jumps to make it to the end)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def jumpingOnClouds(c):
    jump = 0
    i = 0
    while i<len(c)-1:
        if i < len(c)-2 and c[i+2] == 0:
            jump += 1
            i+=2
        elif c[i+1] == 0:
            jump +=1
            i+=1
    return jump
