"""
Exercise: Vowel Counter
Description: Counts how many vowels are entered from lowercase letters until '.' is received.
Constraints: Use exactly one loop.
"""

i=input('Letra: ')
c=0
while i !='.':
    if i in "aeiou":
        c+=1
    i=input('Letra: ')
print(c)