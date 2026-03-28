"""
Exercise: Special Number Check
Description: Checks whether a four-digit number has the property where the sum of its first two digits and last two digits, when squared, equals the original number.
Constraints: Do not use exponentiation or built-in functions.
"""

n = int(input("Digite um número de 4 digitos: "))
n1 = n%100
n2 = n//100
soma=n1+n2
mult=soma*soma
if mult==n:
    print("Sim, é igual")
else:
    print(f"Não, deu {mult}")
