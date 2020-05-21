#!/bin/python3

n, k, q = list(map(int, input().rstrip().split()))

arr = list(map(int, input().rstrip().split()))

while q:
    offset = int(input()) - (k%n)
    if offset < 0:
        offset += n
    print(arr[offset])
    q -= 1