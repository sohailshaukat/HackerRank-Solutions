#!/usr/bin/python

# Head ends here

get_ed = lambda bx,by,dx,dy : abs(dy-by)+abs(dx-bx)

def next_move(posr, posc, board):
    #get first occurences
    dvp = {}
    for i,row in enumerate(iter(board)): 
        if 'd' in row:
            j = row.index('d')
            dvp[get_ed(posc, posr, j, i)] = (j, i)
    nearest_x, nearest_y = dvp[min(dvp.keys())]
    if nearest_y == posr:
        if nearest_x > posc:
            print("RIGHT")
        elif nearest_x < posc:
            print("LEFT")
        else:
            print("CLEAN")
    else:
        if nearest_y > posr:
            print("DOWN")
        else:
            print("UP")
        
    
    
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
