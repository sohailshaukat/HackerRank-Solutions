'''
Arguments: int(number of socks), list(socks in pile)
Output: int(total number of matching pairs)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def sockMerchant(n, ar):
    record = {}
    for el in ar:
        if not el in record:
            record[el] = 1
        else:
            record[el] += 1
    values_list = list(record.values())
    for el in range(0,len(values_list)):
        values_list[el] = int(values_list[el] / 2)
    return sum(values_list)
