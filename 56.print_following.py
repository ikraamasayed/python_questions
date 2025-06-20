#      A 
#     A B 
#    A B C
#   A B C D
#  A B C D E

s=5
a=65
b=" "
for i in range(s):
    for j in range(i,s):
        print(" ",end="")
    for j in range(i+1):
        print(chr(a),end=" ")
        a+=1
    a=65
    print()