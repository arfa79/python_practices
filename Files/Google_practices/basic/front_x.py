# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  sorted_list=[]
  unsorted_list=[]
  for s in words :
    if s[0] == 'x' :        # checking for first alphabet should be x
      sorted_list.append(s)
    else :
      unsorted_list.append(s)
  for u in unsorted_list:
    sorted_list.append(u)    
  return print('sorted list is : ',sorted_list)
front_x (['aba', 'xyz', 'aa', 'x', 'bbb'])