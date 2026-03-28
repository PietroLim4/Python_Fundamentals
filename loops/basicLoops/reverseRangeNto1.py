"""
Exercise: Reverse Range n to 1
Description: Displays all integers from n down to 1.
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
for i in range(n,0,-1):
    print(i, end=' ')