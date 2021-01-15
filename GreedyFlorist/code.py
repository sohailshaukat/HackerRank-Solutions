__, count = map(int, input().rstrip().split())

flowers, bill, run = sorted(map(int, input().rstrip().split())), 0, 1

while flowers:
    for _ in range(count) :
        try:
            bill += flowers.pop() * run
        except:
            break
    run += 1
    
print(bill)
