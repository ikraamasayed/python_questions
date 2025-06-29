#   A B C D E 
#     F G H I 
#       J K L
#         M N
#           O

s=5
a=65
for i in range(s):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,s):
        print(chr(a),end=" ")
        a+=1
    print()

