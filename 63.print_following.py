n=5
p=5

for i in range(n):
    k=p
    for s in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(k,end=" ")
        k-=1
    p-=1
    print()
