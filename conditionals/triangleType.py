"""
Exercise: Triangle Classification
Description: Identifies whether a triangle is equilateral, isosceles, or scalene.
"""

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if b+c>a and c+a>b and b+a>c:
    if a==b and b==c:
        print('Triângulo equilátero')
    else:
        if a==b or a==c or b==c:
            print('Triângulo isósceles')
        else:
            print('Triângulo escaleno')
else:
    print('Não forma triângulo')
