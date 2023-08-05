# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  count = 0
  for s in words :
    if s[0]==s[-1]:               #compare the first alphbet and last
      if len(words) >= 2 :
        count= count +1 
  return print('this is',count)
match_ends (['aba', 'xyz', 'aa', 'x', 'bbb'])