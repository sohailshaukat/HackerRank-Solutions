'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

l = len(a)
swaps = 0
for i in range(l):
    for j in range(l):
        if (not j==l-1) and a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swaps +=1
print(f"Array is sorted in {str(swaps)} swaps.")
print("First Element:",a[0])
print('Last Element:',a[-1])
