'''
Arguments: list(height of candles)
Output: int(no. of candles blown)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def birthdayCakeCandles(ar):
    largest = max(ar)
    counter = 0
    for el in ar:
        if el == largest:
            counter += 1
    return counter
