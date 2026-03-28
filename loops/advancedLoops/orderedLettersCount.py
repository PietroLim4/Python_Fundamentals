# Count uppercase letters read in ascending order until sequence breaks
l=input("Letter: ")
a="A"
c=0
while l>=a:
    c+=1
    a=l
    l=input("Letter: ")
print(c)