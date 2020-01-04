#! python3
'''
problem URL: https://www.hackerrank.com/challenges/leonardo-and-prime/problem?h_r=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
isPrime = [1]*1000000
isPrime[0] = isPrime[1] = 0

ptr = 2
limit = len(isPrime)**0.5
while ptr < limit:
    if isPrime[ptr]:
        fptr = ptr * 2
        while fptr < len(isPrime):
            isPrime[fptr] = 0
            fptr += ptr
    ptr += 1

primes = [i for i, el in enumerate(isPrime) if el == 1]
times = int(input())

for _ in iter(range(times)):
    ptr = 0
    factors = []
    num = int(input())
    prod = 1
    while prod <= num:
        prod *= primes[ptr]
        ptr += 1
    print(ptr-1)
