n=5
count=1
for i in range(n-1):
    for s in range (i,n):
        print(" ",end=" ")

    for num in range(i+1):
        print(count,end=" ")

    for num in range(i):
        print(count,end=" ")
    count+=1
    print()
for i in range (n):
    for s in range (i+1):
        print(" ",end=" ")
    for num in range(i,n):
        print(count,end=" ")
    for num in range(i+1,n):
        print(count,end=" ")
    
    count+=1
    print()
    


