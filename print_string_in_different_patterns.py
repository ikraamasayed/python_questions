s="CODER"
n=len(s)
alpha=0
for i in range(n):
    for a in range(i+1):
        print(s[alpha],end=" ")
    alpha+=1
    print()
print()

alpha=len(s)-1
for i in range(n):
    for a in range(i+1):
        print(s[alpha],end=" ")
    alpha-=1
    print()
print()

for i in range(n):
    alpha=0
    for j in range(i+1):        
        print(s[alpha],end=" ")
        alpha+=1
    print()
print()

k=n-1
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
        p-=1
    print()
    k-=1