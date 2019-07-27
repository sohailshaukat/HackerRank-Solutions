'''
problem URL:https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def wrap(string, max_width):

    i = 1
    l = 0
    arr = []
    while l < len(string):
        if i % (max_width+1) == 0 and i != 0:
            arr.append('\n')
        else:
            arr.append(string[l])
            l += 1
        i += 1
    return ''.join(arr)
