'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
def hourglassSum(arr):
    arr_copy = arr
    l = len(arr)
    final_arr =[]
    new_arr=[]
    for i in range(1, (l-1)):
        x=[]
        for j in range(1, (l-1)):
            x.append( arr_copy[i-1][j-1] + arr_copy[i-1][j] + arr_copy[i-1][j+1] + arr_copy[i][j] + arr_copy[i+1][j-1] + arr_copy[i+1][j] + arr_copy[i+1][j+1] )
        final_arr.append(x)
        print(final_arr)
    for i in final_arr:
        for j in i:
            new_arr.append(j)
        print(new_arr)
    return max(new_arr)
