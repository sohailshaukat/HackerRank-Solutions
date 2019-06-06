'''
Arguments: list(bill / list of cost of items), int( number of item that was ordered for only personA), int(Amount paid by personB )
Output: print(amount owed by any person to another) OR print("Bon Appetit") if it was well split.
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def bonAppetit(bill, k, b):
    extra = bill[k]
    del bill[k]
    split = sum(bill)/2
    if (abs(b-split)):
        print(int(abs(b-split)))
    else:
        print( "Bon Appetit")
