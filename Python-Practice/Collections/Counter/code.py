from collections import Counter

_ = int(input().rstrip())
record = Counter(map(int,input().rstrip().split()))
moni = 0
for _ in iter(range(int(input().rstrip()))):
    size, price = tuple(map(int, input().rstrip().split()))
    if record[size]:
        record[size] -= 1
        moni += price
print(moni)
