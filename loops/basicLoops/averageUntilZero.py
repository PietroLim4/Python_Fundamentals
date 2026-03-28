"""
Exercise: Average Until Zero
Description: Reads real numbers and calculates their arithmetic mean until zero is entered.
Constraints: Use exactly one loop.
"""

n=int(input('Num: '))
s=0
c=0
while n!=0:
    s+=n
    c+=1
    n=int(input('Num: '))
print(f"A média desse números é igual a {s/c:.2f}")