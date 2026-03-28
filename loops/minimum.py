"""
Exercise: Minimum Value Finder
Description: Reads n integers and displays the smallest value.
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
m=int(input('Num: '))
for i in range(n-1):
    v=int(input('Num: '))
    if v<m:
        m=v
print(m)