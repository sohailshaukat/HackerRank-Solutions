'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
#!/bin/python3
# Complete the factorial function below.
def factorial(n):
    if n == 1 or n == 0 :
        fact =  1
    else:
        fact = n * factorial(n-1)
    return fact

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
