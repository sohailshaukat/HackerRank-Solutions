
def bubble_sort(array):
    swaps = 0
    i = 0
    while i < len(array):
        j = 0
        while j < len(array)-1:
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
            j += 1
        i += 1
    return array[0], array[-1], swaps

input()

first, last, swaps = bubble_sort(list(map(int, input().rstrip().split())))

print(f"Array is sorted in {str(swaps)} swaps.\nFirst Element: {str(first)}\nLast Element: {str(last)}")