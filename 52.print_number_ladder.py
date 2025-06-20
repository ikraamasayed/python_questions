a = 5
b=[]

# for int converting before print 
for i in range(1,a+1):
    b.append(i)
    c = str(b).removeprefix("[").removesuffix("]").replace(","," ")
    # print(c)


# for any iterables 
for i in range (1,a+1):
    for j in range(1, i+1):
        print(j,end="  ")
    print()
