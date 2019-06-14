'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_location = a
    house_location_start = s
    house_location_end = t
    orange_location = b
    apples_collected = 0
    oranges_collected = 0
    for i,el in enumerate(apples):
        if house_location_start<=(apple_location + el)<=house_location_end:
            apples_collected += 1
    for j,ek in enumerate(oranges):
        if house_location_start<=(orange_location + ek)<=house_location_end:
            oranges_collected += 1
    print(apples_collected)
    print(oranges_collected)
