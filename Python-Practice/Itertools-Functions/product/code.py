from itertools import product

A = tuple(map(int, input().rstrip().split()))
B = tuple(map(int, input().rstrip().split()))

print(*product(A,B))
