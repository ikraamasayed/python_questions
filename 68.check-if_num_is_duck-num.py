n = 213000

m=n 
count=0
while m!=0:
    d=m%10
    print(d)
    m=m//10
    if  d==0 :
        count+=1
if count >0:
    print("Yes")
else:
    print("No")
print("No of zeros in number:",count)