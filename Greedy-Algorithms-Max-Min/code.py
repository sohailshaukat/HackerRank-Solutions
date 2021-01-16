sample_size, count = [int(input()) for _ in range(2)]

sample_space = sorted([int(input()) for _ in range(sample_size)])
ptr1, ptr2 = 0, count-1

lowest_unfairness = 999999999

while ptr2 < sample_size:
    lowest_unfairness = sample_space[ptr2] - sample_space[ptr1] if lowest_unfairness > sample_space[ptr2] - sample_space[ptr1] else lowest_unfairness
    ptr1, ptr2 = ptr1+1, ptr2+1
    
print(lowest_unfairness)
