#     A 
#    B C
#   D E F
#  G H I J
# K L M N O

aplha = 65
n = 5

for i in range(n+1):

    for j in range(n-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(chr(aplha),end=" ")
        aplha+=1

    print("")