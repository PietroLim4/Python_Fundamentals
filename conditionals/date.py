"""
Exercise: Date Comparison
Description: Determines which of two given dates occurs first.
"""

d1= int(input('Dia 1: '))
m1= int(input('Mes 1: '))
a1= int(input('Ano 1: '))
d2= int(input('Dia 2: '))
m2= int(input('Mes 2: '))
a2= int(input('Ano 2: '))
dt1= a1*10000+m1*100+d1
dt2= a2*10000+m2*100+d2

if dt1>dt2:
    print(d1, m1, a1)
else: 
    print(d2, m2, a2)
