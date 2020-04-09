from collections import defaultdict

record = defaultdict(str)

n, m = tuple(map(int, input().rstrip().split()))

for posi in iter(range(1,n+1)):
    record[input().rstrip()]+=str(posi)+" "

for _ in iter(range(m)):
    tgt = input().rstrip()
    if record[tgt]:
        print(record[tgt])
    else:
        print(-1)
