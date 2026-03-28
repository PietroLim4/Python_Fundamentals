"""
Exercise: Divisibility Check
Description: Determines whether a given integer a is divisible by another integer b.
Constraints: Do not use the remainder operator.
"""

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
div = n1//n2
resul = div*n2
comp = n1-resul
if comp==0:
    print("É divisivel.")
else:
    print("Não é divisivel.")