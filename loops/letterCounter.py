"""
Exercise: Letter Counter
Description: Counts how many letters are entered, one per line, until '.' is received.
Constraints: Use exactly one loop.
"""

i=input('Letra: ')
c=0
while i !='.':
    if i.isalpha() == True:
        c+=1
    i=input('Letra: ')
print(c)