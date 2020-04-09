'''
problem URL: https://www.hackerrank.com/challenges/merge-the-tools/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
from collections import OrderedDict

def setter(u):
    return list(OrderedDict.fromkeys(u))

def merge_the_tools(string, k):
    # your code goes here
    char_list = list(string)
    lower_limit = 0
    upper_limit = k
    length = len(string)
    t = []
    while upper_limit <= length:
        u = list(setter(string[lower_limit:upper_limit]))
        t.append(u)
        lower_limit += k
        upper_limit += k
    t = [''.join(el) for el in t]
    print('\n'.join(t))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    
