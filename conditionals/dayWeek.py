"""
Exercise: Day of the Week
Description: Displays the corresponding day of the week based on an integer input (1–7).
Constraints: If the value is outside the valid range, display "invalid day".
"""

n = int(input("Dia: "))
if n==1:
    print('Domingo')
elif n==2:
    print('Segunda')
elif n==3:
    print('Terça')
elif n==4:
    print('Quarta')
elif n==5:
    print('Quinta')
elif n==6:
    print('Sexta')
elif n==7:
    print('Sabado')
else:
    print("Dia inválido")