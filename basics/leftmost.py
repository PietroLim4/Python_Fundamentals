"""
Exercise: Leftmost Digit
Description: Extracts and displays the first digit of a four-digit integer.
"""

n = int(input('Num: '))
if 1000 <= n <= 9999:
    print(n//1000)
