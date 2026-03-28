"""
Exercise: Sum of Even Values
Description: Reads n integers and displays the sum of the even values only.
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
s=0
for i in range(n):
    v=int(input('Digite o que somar: '))
    if v%2==0:
        s+=v
print(s)