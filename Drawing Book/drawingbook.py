'''
Arguments: int(last page number / no. of pages in book), int(destination page number)
Output: int(minimum no. of turns)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def pageCount(n, p):
    forward_turns = math.ceil((p-1)/2)
    reverse_turns = ((n-p)/2)
    if p%2==0:
        reverse_turns = math.floor(reverse_turns)
    else:
        reverse_turns = math.ceil(reverse_turns)
    return min(forward_turns,reverse_turns)
