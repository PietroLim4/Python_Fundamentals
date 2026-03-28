"""
Exercise: Maximum of Three Values
Description: Finds and displays the largest value among three distinct real numbers.
"""

a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
maior=a
if b>=a:
    maior=b
if maior<=c:
    maior=c
print("O maior número é ", maior)
