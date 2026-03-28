# Check if a number can be expressed as the product of three consecutive integers
n=int(input("Num: "))
cont=0
while cont*(cont+1)*(cont+2)<n:
    cont+=1
if cont*(cont+1)*(cont+2)==n:
    print("Triangular")
else:
    print("Not triangular")