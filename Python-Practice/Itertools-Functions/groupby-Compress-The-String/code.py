from itertools import groupby

string = input().rstrip()

print(*[(len(list(group)), int(el)) for el,group in groupby(string)])
