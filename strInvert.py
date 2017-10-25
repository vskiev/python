#!/usr/bin/python
s = "Invert me please"
print(s)
print("=========="*4)
def inv1(string):
   lst =  list(string)
   lst.reverse()
   newstr=''.join(lst)
   return newstr

print(inv1(s))

print("=========="*4)
def inv2(string):
    newstr=string[::-1]
    return newstr

print(inv2(s))

print("=========="*4)

def inv3(string):
 lst1 = list()
 for i in range(len(string)-1, -1, -1):
  lst1.append(string[i])
  newstr = ''.join(lst1)
 return newstr

print(inv3(s))

