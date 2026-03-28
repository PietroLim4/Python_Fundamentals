"""
Exercise: Salary Adjustment
Description: Calculates a new salary by increasing the current salary by a percentage equal to the person's age.
"""

salario = float(input('Salário: '))
idade = int(input('Idade: '))
porc = idade/100
aum = porc*salario
print(f'Novo salário: R$ {(salario + aum):.2f}')