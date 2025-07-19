# composit num are those num which has more than 1 factor than 1 & it's self

take_input= int(input("enter the number: "))
factor_list= []
for i in range (1,take_input+1):
    if take_input%i==0:
        factor_list.append(i)
if len(factor_list) >=2:
    print(True,len(factor_list))
else:
    print(False,len(factor_list))

# other way
count=0
for i in range(1,take_input+1):
    if take_input%i==0:
        count+=1
if count > 2:
    print(True,count)
else :
    print(False,count)