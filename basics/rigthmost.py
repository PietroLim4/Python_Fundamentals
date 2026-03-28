"""
Exercise: Rightmost Digit
Description: Extracts and displays the last digit of a non-negative integer.
Constraints: Use the remainder operator (%).
"""

n = float(input('Digite um número: '))
if n>=0:
    print('O digito mais a direita é: ',n%10)
