"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array)<= 1:
        return array
    pivot = array [0]  #choosing the first element of array as pivot 
    # make partition in two list 
    right = [x for x in array[1:] if x >= pivot] 
    left = [x for x in array[1:] if x < pivot]

    return quicksort(left) + [pivot] + quicksort(right) # recursivly take back the quicksort for sorting 
       
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))