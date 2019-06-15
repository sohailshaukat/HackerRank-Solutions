'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
if __name__ == '__main__':
    n = int(input())
    big_counter = 0
    binary_n = bin(n)
    for i,el in enumerate(binary_n[2::]):
        if el == '1':
            counter = 0
            for j,ek in enumerate(binary_n[i::]):
                if ek == '0':
                    break
                elif ek == '1' :
                    counter += 1
            if counter > big_counter:
                big_counter = counter
    print(big_counter)
