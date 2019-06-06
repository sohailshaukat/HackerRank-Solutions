'''
Arguments: int(year)
Output: str(date of day of the programmer in that year)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def isLeap(year):
    if year > 1918:
        return (year%4==0 and (not year%100==0 or year%400==0))
    elif year < 1918:
        return year%4==0
    return
def dayOfProgrammer(year):
    if year==1918:
        return f"26.09.{year}"
    else:
        if isLeap(year):
            return f"12.09.{year}"
        else :
            return f"13.09.{year}"
