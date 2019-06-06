'''
Arguments: int(catA position),int(catB position), int(mouseC position)
Output: str(Winner)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def catAndMouse(x, y, z):
    d_x = abs(z-x)
    d_y = abs(z-y)
    if d_x == d_y:
        return "Mouse C"
    elif d_x > d_y :
        return "Cat B"
    else:
        return "Cat A"
