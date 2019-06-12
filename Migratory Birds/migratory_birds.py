'''
Arguments: list(bird entries)
Output: int(most frequent bird)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def migratoryBirds(arr):
    arr = sorted(arr)
    counter = {}
    frequency = 0
    for el in arr:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    for i,ek in counter.items():
        if ek > frequency:
            frequency = ek
            frequent = i
    return frequent
