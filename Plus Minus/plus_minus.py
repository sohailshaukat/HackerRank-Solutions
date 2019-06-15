'''
Arguments: list(of integers)
Output: float(probabilities of positive, negative and zeroes)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def plusMinus(arr):
    numbers = {'positive':0, 'negative': 0, 'zeroes':0 }
    l = len(arr)
    for i,el in enumerate(arr):
        if el >0:
            numbers['positive']+=1
        elif el<0:
            numbers['negative']+=1
        else:
            numbers['zeroes']+=1
    print(numbers['positive'] / l)
    print(numbers['negative']/ l)
    print(numbers['zeroes'] / l)
