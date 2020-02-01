#! python3
'''
problem URL: https://www.hackerrank.com/challenges/best-divisor/copy-from/137648115?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
from functools import reduce
from operator import add

def divisors(num):
    '''
    This function takes int and returns a list of divisors O(n^0.5)
    '''
    div = []
    ptr = 1
    while ptr <= num**0.5:
        if not (num%ptr):
            div.append(ptr)
            div.append(num//ptr)
        ptr += 1
    return set(div)

# def addMe(x):
    # '''
    # This function takes in int and returns a list int and sum of all the digits
    #     e.g. [26, 8] 
    # '''
    # score = [x,0]
    # for el in list(str(x)):
    #     score[1] += int(el)
    # return score

addMe = lambda x : [x, reduce(add,map(int,list(str(x))))]

if __name__ == "__main__":
    num = int(input())

    score_arr = list(map(addMe, divisors(num)))

    max_score = 0
    favorite = None

    for score in score_arr:
        if score[1] > max_score:
            max_score = score[1]
            favorite = score[0]
        elif score[1] == max_score:
            favorite = min(score[0], favorite) 

    print(favorite)





