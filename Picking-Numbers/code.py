#! usr/bin/python3

length = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

elements = set(arr)
element_count = len(elements)
occurences = dict(zip(elements,[0]*element_count))

maximum_occurences = 0

for element in iter(arr):
    occurences[element] += 1
    if occurences[element] > maximum_occurences:
        maximum_occurences = occurences[element]

elements = list(elements)
maximum_length = maximum_occurences

ptr = 0
while ptr < element_count-1:
    tptr = elements[ptr]
    hptr = elements[ptr+1]
    if hptr - tptr == 1:
        if occurences[tptr]+occurences[hptr] > maximum_length:
            maximum_length = occurences[tptr]+occurences[hptr] 
    ptr += 1

print(maximum_length)

