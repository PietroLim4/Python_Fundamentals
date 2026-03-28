"""
Exercise: Quadratic Equation Solver
Description: Calculates the real roots of a quadratic equation based on its coefficients.
Constraints: If the discriminant is negative, display that no real roots exist.
"""

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

delta= b*b-4*a*c

if delta < 0:
    print('Não existem raizes reais.')
else:
    raiz = delta**0.5
    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)

    print(f'x1 = {x1:.2f}')
    print(f'x2 = {x2:.2f}')