n= 123
m=n
sum= 0
prod=1

while m!=0:
    d=m%10 # returns the remainder i.e 3,2,1,
    print("d:",d)
    m =m //10 # returns the 12,1,0
    print(m)

    sum +=d #3+2+1 = 6
    prod *=d #3*2*1 = 6

if sum == prod:
    print(f"yes , sum:{sum} , prod :{prod}")
else:print(f"no , sum:{sum} , prod :{prod}")