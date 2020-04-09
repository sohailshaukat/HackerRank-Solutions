from collections import OrderedDict

record = OrderedDict()

for _ in iter(range(int(input().rstrip()))):
    item, sep, price = input().rpartition(" ")
    record[item] = record.get(item,0)+int(price)

for item,price in iter(record.items()):
    print(item,price)
