'''
Arguments: list(scores)
Output: int(record high), int(record low)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def breakingRecords(scores):
    record_low = scores[0]
    record_high = scores[0]
    record_low_break = 0
    record_high_break = 0
    for el in scores[1:]:
        if el < record_low:
            record_low = el
            record_low_break += 1
        elif el > record_high:
            record_high = el
            record_high_break += 1
    return record_high_break,record_low_break
