a=int(input())
b=list(map(int, input().split()))
max=b[0]
min=b[0]

for n in range(a):
    if b[n]>max:
        max=b[n]
        
for n in range(a):
    if b[n]<min:
        min=b[n]

print(max, min)
    
