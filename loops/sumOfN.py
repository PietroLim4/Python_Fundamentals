"""
Exercise: Sum of n Values
Description: Reads n integers and displays their sum (excluding the value of n).
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
s=0
for i in range(n):
    v=int(input('Digite o que somar: '))
    s+=v
print(s)