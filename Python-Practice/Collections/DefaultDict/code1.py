from collections import defaultdict

def im_here(tgt, record):
    for i,el in enumerate(iter(record)):
        if el == tgt:
            yield i+1


n, m = tuple(map(int, input().rstrip().split()))

record = defaultdict(list)
for _ in iter(range(n)):
    record['A'].append(input().rstrip())

for _ in iter(range(m)):
    tgt = input().rstrip()
    if tgt not in record['A']:
        print(-1)
    else:
        print(*im_here(tgt, record['A']))
