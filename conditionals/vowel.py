"""
Exercise: Vowel Identification
Description: Determines whether a given character is a vowel.
"""

l = str(input("Digite uma letra: "))
if l.lower() in "aeiou":
    print("É vogal.")
else:
    print("Não é vogal")
