'''
Arguments: string(Main string), string(substring)
Output: int(no. of time substring occurs in Main string)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def count_substring(string, sub_string):
    counter = 0
    while string.find(sub_string) >= 0:
        counter += 1
        string = string[string.find(sub_string)+1::]
    return counter
