A,B=list(map(str,input().split()))

a=0
b=0

for n in range(len(A)):
    a=a+int(A[n])*(10**n)
    
for n in range(len(B)):
    b=b+int(B[n])*(10**n)

if a>b:
    print(a)
else:
    print(b)
