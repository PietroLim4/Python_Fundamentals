"""
Exercise: Split Sum
Description: Splits a four-digit number into two parts (first two digits and last two digits) and displays their sum.
"""

n = int(input('Num: '))
if  1000 <= n <= 9999:
    n1 = n//100
    n2 = n%100
    print(n1+n2)
