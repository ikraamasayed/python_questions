n=5 
p=1
for i in range(n-1):

    #spacing 
    for j in range(i,n):
        print(" ",end=" ")

    #print nums 
    #       1 
    #     2 2 
    #   3 3 3 
    # 4 4 4 4 

    for j in range(i+1):
        print(p,end=" ")

    # 2
    # 3 3
    # 4 4 4

    for j in range(i):
        print(p,end=" ")
    p+=1
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")

#   5 5 5 5 5
    # 4 4 4 4
    #   3 3 3
    #     2 2
    #       1
    for j in range(i,n):
        print(p,end=" ")

    # 5 5 5 5
    # 4 4 4
    # 3 3 
    # 2 
    for j in range(i+1,n):
        print(p,end=" ")

    p-=1
    print()

#square plus
#         4
#         4
#         4
#         4
# 4 4 4 4 4 4 4 4 4
#         4
#         4
#         4
#         4
m= 9
for i in range(m):
    for j in range(m):
        if i==m//2 :
            print(i , end=" ")
        elif j==m//2:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()


#X
# 0               0
#   1           1
#     2       2
#       3   3
#         4
#       5   5
#     6       6
#   7           7
# 8               8

k= 9
for i in range(k):
    for j in range(k):
        if i==j or i+j == k-1 :
            print(i,end=" ")
        else :
            print(" ",end=" ")
    print()


#square
side =9
for i in range(side):
    for j in range(side):
        if i==0 or i==side-1 or j ==0 or j==side-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()