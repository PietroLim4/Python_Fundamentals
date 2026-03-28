# Convert a decimal number to binary without built-in functions
n=int(input("Num: "))
b=""
while n>0:
    if n%2==1:
        b=b+"1"
    else:
        b=b+"0"
    n=n//2
b=b[::-1]
print(b)