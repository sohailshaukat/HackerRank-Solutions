'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import math
times = int(input())
while times:
    num = int(input())
    limit = int(math.sqrt(num))+1
    i = 2
    prime = True
    while i <= limit:
        if (num%i == 0 or num == 0 or num == 1 )and not num == 2:
            print('Not prime')
            prime = False
            break
        i+=1
    if prime:
        print('Prime')
    times -=1
