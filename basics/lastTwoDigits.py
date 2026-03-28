"""
Exercise: Last Two Digits Extraction
Description: Displays the last two digits of an integer greater than 10.
Constraints: Do not use the remainder operator.
"""

n = input('Número: ')
if int(n) > 10:
    print(n[-2:])
