"""
Exercise: Sum Until Zero
Description: Reads integers and displays their sum until zero is entered.
Constraints: Use exactly one loop.
"""

s=0
while True:
    n=int(input('Num: '))
    if n!=0:
        s+=n
    else:
        break
print(s)