def ladder(n):
    count = 1
    for i in range (0,n):
        for j in range(0,i+1):
            print(count,end=" ")
            count+=1
        print()

# print(ladder(5))


s= 5
p= 1
for i in range (1,s+1):
    for j in range (1,i+1):
        print(p,end=" ")    #will replace p with j for number ladder code 
        p+=1
    print()