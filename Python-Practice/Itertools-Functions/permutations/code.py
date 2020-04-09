from itertools import permutations

word, set_length = input().rstrip().split()

print(*sorted(map("".join,permutations(word, int(set_length)))), sep='\n')
