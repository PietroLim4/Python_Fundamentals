"""
Exercise: Final Grade Calculation
Description: Calculates a student's final grade based on weighted scores (40% + 40% + 20%).
Constraints: Display the result with two decimal places.
"""

p1 = float(input('Nota da prova 1: '))
p2 = float(input('Nota da prova 2: '))
tr = float(input('Nota dos trabalhos: '))
p1_porc = p1*0.4
p2_porc = p2*0.4
tr_porc = tr*0.2
total = p1_porc+p2_porc+tr_porc
print(f"Nota final é: {total:.2f}")
