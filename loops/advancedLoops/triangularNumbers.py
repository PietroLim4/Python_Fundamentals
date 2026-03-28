# Generate the first N terms of the triangular number sequence (1 + 2 + ... + n)
n=int(input("Num: "))
p=0
for i in range(1, n+1, 1):
    p+=i
    print(p, end=' ')