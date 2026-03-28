"""
Exercise: Multiples of 3
Description: Displays all multiples of 3 up to a maximum value n.
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
for i in range(3, n, 3):
    print(i, end=' ')