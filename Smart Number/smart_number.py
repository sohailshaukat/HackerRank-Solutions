'''
Arguments: int(number)
Output: str(YES or NO)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / (val*val) == 1:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
