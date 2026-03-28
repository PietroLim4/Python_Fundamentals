"""
Exercise: Integer Division Without Operators
Description: Calculates the integer division of p by q without using division, multiplication, or exponentiation.
Constraints: Use exactly one loop.
"""

p=int(input('Num: '))
q=int(input('Num: '))
c=0
while p>=q:
    p-=q
    c+=1
print(c)