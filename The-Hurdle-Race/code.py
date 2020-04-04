#! usr/bin/env python3
size, max_height = tuple(map(int, input().rstrip().split()))
heights = list(map(int, input().rstrip().split()))
max_hurdle = max(heights)
print(max(0,max_hurdle-max_height))