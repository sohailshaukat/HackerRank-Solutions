#

def nextMove(n,r,c,grid):
    #to find princess
    for i,row in enumerate(iter(grid)):
        if 'p' in row:
            princess_y, princess_x = (i,row.find('p'))
    if princess_y == r:
        if princess_x > c:
            return("RIGHT")
        else :
            return("LEFT")
    else:
        if princess_y > r:
            return("DOWN")
        else:
            return("UP")
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
