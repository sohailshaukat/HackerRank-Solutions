#!pyhton3
'''
problem URL: https://www.hackerrank.com/challenges/sherlock-and-divisors/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!python3

def get_factors(num):
    factor_count = 0
    ptr = 1
    while ptr <= num**0.5:
        if (not (num % ptr)):
            if not(ptr % 2):
                factor_count += 1
            if ptr != num**0.5:
                if not((num//ptr) % 2):
                    factor_count += 1
        ptr += 1
    return factor_count


times = int(input())

for _ in iter(range(times)):
    num = int(input())
    print(get_factors(num))
