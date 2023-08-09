"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0:  # the 1th number of fibonacci is 0 and for fast result returning when equal
        return 0
    if position == 1 or position == 2 : # the 2th and 3th numbers of fibonacci are 1 and for fast result returning them when they equal
        return 1
    fib = get_fib(position - 1) + get_fib (position - 2) # calling the def recursivly for findeing two number beforea and value in result of fib
    return fib
# Test cases
print( get_fib(9))
print( get_fib(11))
print( get_fib(0))

