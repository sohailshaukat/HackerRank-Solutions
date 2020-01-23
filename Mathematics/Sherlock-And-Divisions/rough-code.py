#!pyhton3
'''
problem URL: https://www.hackerrank.com/challenges/sherlock-and-divisors/problem
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
# def is_uniquely_even(num):
#     return not(num%2)

def get_factors(num):
    # factors = []
    factor_count = 0
    ptr = 1
    while ptr <= num**0.5:
        if (not (num%ptr) ) :
            if not(ptr%2):
                factor_count += 1
            # factors.append(ptr)
            if ptr != num**0.5:
                if not((num//ptr)%2):
                    factor_count += 1
                # factors.append(num//ptr)
        ptr += 1
    # return list(filter(is_uniquely_even, factors))
    return factor_count
times = int(input())

for _ in iter(range(times)):
    num = int(input())
    # print(len(get_factors(num)))
    print(get_factors(num))

