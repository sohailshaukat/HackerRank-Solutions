'''
Arguments: list(list of String), list(queries)
Output: list(occurences of queries in strings)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def matchingStrings(strings, queries):
    record = [0]*len(queries)
    for i,el in enumerate(queries):
        for k,ek in enumerate(strings):
            if el == ek:
                record[i]+=1

    return record
