char_count = {}
flag = 1
def refToDict(char):
    global char_count, flag
    if char_count.get(char, False):
        char_count[char] += flag
    else:
        char_count[char] = flag
    return char

a = list(map(refToDict, list(input())))

flag = -1

b = list(map(refToDict, list(input())))

del flag

removal = 0
for value in char_count.values():
    if value != 0:
        removal += abs(value)

print(removal)