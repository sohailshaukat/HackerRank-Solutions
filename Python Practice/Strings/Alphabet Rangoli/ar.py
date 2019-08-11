'''
problem URL: https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=false
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def frameSetter(char_list, line_number):
    frame = (char_list[:line_number+1:])
    rev_frame = (frame[:line_number:])
    return ('-').join(frame+rev_frame[::-1])

def print_rangoli(size):
    # your code goes here
    char_list = [chr(num) for num in range(97,97+size)]
    char_list = char_list[::-1]
    rev_frame_stack = []
    for line_number in range(0,2*size):
        if line_number < size-1:
            frame = frameSetter(char_list, line_number)
            rev_frame_stack.append(frame)
            print(frame.center(4*size-3,'-'))
        elif line_number == size-1:
            frame = frameSetter(char_list, line_number)
            print(frame.center(4*size-3,'-'))
        elif line_number < 2*size-1:
            print(rev_frame_stack.pop().center(4*size-3,'-'))
