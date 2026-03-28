# Reverse the digits of an integer using arithmetic operations
n=int(input("Num: "))
while n>0:
    print(n%10, end='')
    n=n//10