'''
Arguments: list(grades)
Output: list(rounded off grades)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def gradingStudents(grades):
    for i,el in enumerate(grades):
        if el>37:
            x = int(el/5)
            x+=1
            nextMultiple = x*5
            if (nextMultiple-el) < 3:
                grades[i] = nextMultiple
    return( grades)
