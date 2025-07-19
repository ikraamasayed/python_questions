lst1 = [1,3,5]
lst2 = [2,4,6]


lst4=[] # adding two element with same index 
if len(lst1) == len(lst2):
    for i in range(0,len(lst2)):
        lst4.append(lst1[i] + lst2[i])
    print(lst4)
else: 
    print(f"len is not same ")