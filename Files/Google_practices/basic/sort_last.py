# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def reverse(tuples):
  return tuples[-1]               #return last tuple
def sort_last(tuples):
  sorted_last=[]
  sorted_last=sorted(tuples, key=reverse)     #we used reverse as key for sorting 
  return print(sorted_last)
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])