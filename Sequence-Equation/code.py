#!/bin/python3

input()

sequence = list(map(int,input().rstrip().split()))
index_cache = {}

for i,element in iter(enumerate(sequence)):
    index_cache[element] = i+1

print(*[index_cache[index_cache[index_cache[element]]] for element in iter(sequence)], sep="\n")
