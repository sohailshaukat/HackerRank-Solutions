'''
problem URL: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
if __name__ == '__main__':
    s = input()
    flags = {"alphanumeric":False, "alphabetical":False, "digits":False, "lowercase":False, "uppercase":False}
    for el in s:
        if el.isalnum() and not flags["alphanumeric"]:
            flags["alphanumeric"] = True
        if el.isalpha() and not flags["alphabetical"]:
            flags["alphabetical"] = True
        if el.isdigit() and not flags["digits"]:
            flags["digits"] = True
        if el.islower() and not flags["lowercase"]:
            flags["lowercase"] = True
        if el.isupper() and not flags["uppercase"]:
            flags["uppercase"] = True
        if flags["alphanumeric"] and flags["alphabetical"] and flags["digits"] and flags["lowercase"] and flags["uppercase"]:
            break
    print(flags["alphanumeric"])
    print(flags["alphabetical"])
    print(flags["digits"])
    print(flags["lowercase"])
    print(flags["uppercase"])
