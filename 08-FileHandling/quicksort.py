import math

def quicksort(array, start=0, end=-5):
    if end == -5:
        end = len(array)-1
    
    if(start>=end):
        return
    
    pivot = array[math.floor(end/2)]

    left= start
    right = end
    while(left<right):
        if array[left] < pivot:
            left+=1
        else:
            temp_left = array[left]
            array[left] = array[right]
            array[right] = temp_left
            right-=1

    if(start<left-1):
        quicksort(array, start, left-1)
    if (right<end):
        quicksort(array, right, end)

arr = [1,3,5,4,6,1,3,6,11]

quicksort(arr)

for e in arr:
    print(e)
            


