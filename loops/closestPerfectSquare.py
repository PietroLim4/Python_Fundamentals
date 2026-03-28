"""
Exercise: Largest Perfect Square
Description: Finds the largest perfect square less than or equal to a given number n.
Constraints: Do not use exponentiation, built-in functions, or type conversion. Use exactly one loop.
"""

n=int(input('Num: '))
m=0
while m*m<=n:
    m+=1
m-=1
print(m*m) 
    