"""
Exercise: Reverse Range with Count (n-1 to 0)
Description: Displays integers from n-1 down to 1.
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
for i in range(n-1, 0, -1):
    print(i, end=' ')