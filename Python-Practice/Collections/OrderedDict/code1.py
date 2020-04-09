from collections import OrderedDict

record = OrderedDict()

for _ in iter(range(int(input().rstrip()))):
    line = input().rstrip().split()
    try :
        record[" ".join(line[:-1:])] += int(line[-1])
    except:
        record[" ".join(line[:-1:])] = int(line[-1])

custom_joint = lambda el : el[0]+" "+str(el[1])

print(*map(custom_joint,record.items()), sep='\n')
