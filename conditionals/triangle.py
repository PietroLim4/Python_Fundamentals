"""
Exercise: Triangle Validation
Description: Checks whether three given segments can form a triangle.
"""

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if b+c>a and c+a>b and b+a>c:
    print('Formam triângulo')
else:
    print('Não formam triângulo')
