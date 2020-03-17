#! usr/bin/python3

'''

A boundary set would be an object that would contain only minimum and maximum value of that set reducing the space complexity to constant.

For each 'el'
    check for compatible set
        if yes
            add to that set, boundary set could be used.
        if no
            create new set

'''
from collections import namedtuple



def isCompatible(el, sets):
    if sets == []:
        return False
    for i,s in enumerate(iter(sets)):
        if s.lower-1 <= el <= s.upper+1 :
            return i 

length = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

sets = []

for i,el in enumerate(iter(arr)):
    compatibleWith = isCompatible(el,sets):
    if compatibleWith is False:
        