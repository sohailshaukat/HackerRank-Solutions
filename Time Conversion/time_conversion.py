'''
Arguments: str(time)
Output: str(time converted)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def timeConversion(s):
    meridian = s[-2:]
    time = s[:-2].split(':')
    hour = time[0]
    if meridian == 'PM' and not hour == '12':
        hour = int(hour) + 12
        hour = str(hour)
    if hour == '12' and meridian == 'AM':
        hour = '00'
    time[0] = (hour)
    time_str = ':'.join(time)
    return(time_str)
