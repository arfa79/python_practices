def match_ends(words):
  # +++your code here+++
  count = 0
  for s in words :
    if s[0]==s[-1]:
      if len(words) >= 2 :
        count= count +1 
  return print('this is',count)
match_ends (['aba', 'xyz', 'aa', 'x', 'bbb'])