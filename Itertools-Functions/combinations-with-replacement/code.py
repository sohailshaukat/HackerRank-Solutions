from itertools import combinations_with_replacement

word, set_length = input().rstrip().split()

print(*map(''.join,combinations_with_replacement(sorted(word), int(set_length))), sep="\n")
