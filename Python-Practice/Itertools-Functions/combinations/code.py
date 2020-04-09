from itertools import combinations

word, set_length = input().rstrip().split()

for length in iter(range(1,int(set_length)+1)):
    print(*map("".join,combinations(sorted(word),length)), sep="\n")
