"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    lowest = 0                    # in this code use the low and hight for indexing
    highest = len(input_array) -1  
    while lowest <= highest :
        middle = (highest+lowest)//2        # middle index is the result of high and low avrage         
        middle_value = input_array[middle]
        if middle_value == value:
            return middle
        elif middle_value < value :
            lowest = middle + 1    # lowest index needs to plus 1 to get close to valus index 
        else :
            highest = middle - 1   # highest index needs to minus 1 to get close to valus index 
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))