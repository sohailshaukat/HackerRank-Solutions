#! usr/bin/env python3
l = 2
total = 2
for _ in iter(range(1,int(input()))):
    l += l >> 1
    total += l

print(total)