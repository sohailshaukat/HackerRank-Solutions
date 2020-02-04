'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def kangaroo(x1, v1, x2, v2):
    fast_kang_speed = max(v1,v2)
    slow_kang_speed = min(v1,v2)
    if fast_kang_speed == v1:
        fast_kang_pos = x1
        slow_kang_pos = x2
    else :
        fast_kang_pos = x2
        slow_kang_pos = x1
    while fast_kang_pos <= slow_kang_pos and not fast_kang_speed == slow_kang_speed :
        if fast_kang_pos == slow_kang_pos:
            return "YES"
        fast_kang_pos += fast_kang_speed
        slow_kang_pos += slow_kang_speed
    return "NO"
