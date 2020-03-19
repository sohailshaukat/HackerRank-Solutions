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
class BoundarySet:

    def __init__(self, key):
        self.lower = key
        self.upper = key
        self.length = 1
        self.elements = [key]

    def __repr__(self):
        # return "L: "+str(self.lower)+" U: "+str(self.upper)
        return "->".join(map(str,self.elements))

def isCompatible(el, sets):
    if sets == []:
        return False
    for i,s in enumerate(iter(sets)):
        if s.lower-1 <= el <= s.upper :
            return i 
    return False


length = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

sets = []

maximum_length = 1

for i,el in enumerate(iter(arr)):
    compatibleWith = isCompatible(el,sets)
    if compatibleWith is False:
        new_set = BoundarySet(el)
        sets.append(new_set)
    else:
        sets[compatibleWith].elements.append(el)
        sets[compatibleWith].length += 1
        if el < sets[compatibleWith].lower:
            sets[compatibleWith].lower -= 1
    if sets[compatibleWith].length > maximum_length:
        maximum_length = sets[compatibleWith].length

print(maximum_length)


