"""
Exercise: Interval Check
Description: Verifies whether a number n is within a given closed interval [a, b].
"""

n = int(input("Número: "))
a = int(input("Começo do intervalo: "))
b = int(input("Fim do intervalo: "))
if n>=a and n<=b:
    print(f"{n} está no intervalo.")
else:
    print(f"{n} está fora desse intervalo.")
