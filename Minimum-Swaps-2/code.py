#! usr/env/bin python3

input()
sequence = list(map(int,input().rstrip().split()))

index_cache = {}
for i, el in iter(enumerate(sequence)):
    index_cache[el] = i

swaps = 0
while i:
    el = sequence[i]
    if i!=el-1:
        sequence[i], sequence[index_cache[i+1]] = sequence[index_cache[i+1]], sequence[i]
        
        index_cache[el], index_cache[i+1] = index_cache[i+1], index_cache[el]

        swaps += 1
    i -= 1

print(swaps)
