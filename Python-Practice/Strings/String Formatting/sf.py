'''
problem URL: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def print_formatted(number):
    # your code goes here
    width = len(str(bin(number).replace('0b','')))
    for num in range(1,number+1):
        binary = str(bin(num).replace('0b',''))
        octal = str(oct(num).replace('0o',''))
        hexadecimal = str(hex(num).replace('0x','')).upper()
        if num < number:
            print(str(num).rjust(width)+" "+octal.rjust(width)+" "+hexadecimal.rjust(width)+" "+binary.rjust(width))
        else:
            print(str(num).rjust(width)+" "+octal.rjust(width)+" "+hexadecimal.rjust(width)+" "+binary.rjust(width), end = '')
