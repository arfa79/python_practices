# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  # LAB(begin solution)
  for s in list2:       # for joining every string one by one and not as list
    list1.append(s)     # joining two lists togrther for better sorting
  result=sorted(list1)  # use sorted method for sorting the string list  
  return print(result)
linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])


  