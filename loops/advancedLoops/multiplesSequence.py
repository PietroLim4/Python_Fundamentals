# Generate the first N multiples of A or B in ascending order without repetition
a=int(input("A "))
b=int(input("B "))
n=int(input("N "))
count=0
aMult=1
bMult=1
while count<n:
    ta=a*aMult
    tb=b*bMult
    if ta>tb:
        print(tb, end=' ')
        bMult+=1
    elif tb>ta:
        print(ta, end=' ')
        aMult+=1
    else:
        print(ta, end=' ')
        aMult+=1
        bMult+=1
    count+=1