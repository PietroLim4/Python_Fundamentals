"""
Exercise: Reverse Range with Count (n-1 to 0)
Description: Displays integers from n-1 down to 0.
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
for i in range(n-1, -1, -1):
    print(i, end=' ')