#!/usr/bin/env python3.6
# Examples:
#
# • foefet is an anagram of toffee
#
# • Buckethead is an anagram of DeathCubeK

w1 = "Buckethead"
w2 = "DeathCubeK"

w3 = "сирота"
w4 = "DeathC"

w5 = "foefet"
w6 = "toffee"

def is_Anagram(test, original):

 flag = True

 test =  sorted(test.lower())
 original =  sorted(original.lower())

 if len(test) == len(original):
  for i,j in zip(test, original):
   flag = str(i).__eq__(str(j))
   if flag == False : return False
 else:
   flag = True
 return flag

print(is_Anagram(w1 ,w2))
print(is_Anagram(w3 ,w4))
print(is_Anagram(w5 ,w6))

