import numpy as np
str1=input('Enter string:')
def helper(i,j,st):
  if i==0 or j==0:
    return 0
  if st[i-1] ==st[j-1] and i!=j:
    return 1+ helper(i-1,j-1,st)
  return max(helper(i-1,j,st),helper(i,j-1,st))
def lrs(str1):
  n=len(str1)
  return helper(n,n,str1)
final=lrs(str1)
print(final
