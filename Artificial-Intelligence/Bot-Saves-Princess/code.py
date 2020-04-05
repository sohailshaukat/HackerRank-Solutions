#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    if grid[0][0]=="p":
        for _ in iter(range(0,(n-1)//2)):
            print("UP")
            print("LEFT")    
    elif grid[0][n-1]=="p":
        for _ in iter(range(0,(n-1)//2)):
            print("UP")
            print("RIGHT")    
    elif grid[n-1][0]=="p":
        for _ in iter(range(0,(n-1)//2)):
            print("DOWN")
            print("LEFT")    
    else:
        for _ in iter(range(0,(n-1)//2)):
            print("DOWN")
            print("RIGHT")        
    
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
