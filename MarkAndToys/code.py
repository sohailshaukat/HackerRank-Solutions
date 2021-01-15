_, amount = map(int, input().rstrip().split())
prices = list(map(int, input().rstrip().split()))


total = 0
items = 0
while prices:
    total += prices.pop(prices.index(min(prices)))
    if total <= amount:
        items += 1
    else: 
        break
    
    
print(items)
