'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
actual_return_date = input()
expected_return_date = input()
actual_return_date_list = actual_return_date.split(" ")
expected_return_date_list = expected_return_date.split(" ")

ard_day = int(actual_return_date_list[0])
ard_month = int(actual_return_date_list[1])
ard_year = int(actual_return_date_list[2])
erd_day = int(expected_return_date_list[0])
erd_month = int(expected_return_date_list[1])
erd_year = int(expected_return_date_list[2])



if ard_year > erd_year:
    print("10000")
elif ard_year < erd_year:
    print("0")
else:
    if ard_month > erd_month:
        delay = ard_month - erd_month
        fine = delay * 500
        print(fine)
    else:
        if ard_day > erd_day:
            delay = ard_day - erd_day
            fine = delay* 15
            print(fine)
        else:
            print("0")
