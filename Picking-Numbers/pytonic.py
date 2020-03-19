#! usr/bin/python3

length = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

print(max([sum((arr.count(i), arr.count(i+1))) for i in set(arr)]))

