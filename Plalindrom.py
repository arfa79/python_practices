# i will write a program that reads same in right to left and left to right 

def isPalindrome(x: int) -> bool:
    stringx=str(x)
    splitx=stringx.split()
    print (splitx)
    '''for n in splitx and range(len(splitx) - 1, -1, -1) :
        reverse_string=''
        reverse_string =reverse_string + n
    if reverse_string == stringx :
        print ('that is palindrome')
    else:
        print('that is Not a plaindrome')

    return''' 
    '''binaryx=bin(x)[2:]
    num=x
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
        #print (reversed_num)
    binary_reversed_num=bin(reversed_num)[2:]
    #print(binary_reversed_num)
    if binary_reversed_num == binaryx :
        return print('thats is palindrome')
    else :
        return print('that is not palindrome')'''
isPalindrome(-323)