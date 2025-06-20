# A
# B B 
# C C C 
# D D D D
# E E E E E 


s=5
a=65
for i in range (s):
    for j in range(i+1):
        print(chr(a),end=" ")
    a+=1
    print()