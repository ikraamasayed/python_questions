aplha = 65
n = 5


for i in range(n+1):

    for j in range(n-i):
        print(" ",end="")

    for j in range(i+1):
        print("*",end=" ")

    print("")

n=5
for i in range(n+1):

    for j in range(n-i):
        print(" ",end=" ")

    for j in range(i+1):
        print("*",end=" ")

    for j in range(i):
        print("*",end=" ")
    print("")