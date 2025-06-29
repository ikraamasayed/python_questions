#check if the number is neon number. Number,digits of whose square are equal to the number itself.

n= 9
m=n**2
sum= 0 
while m!=0:
    print(f"m: {m}")
    d=m%10
    print(f"d: {d}")
    sum=sum+d
    print(f"sum: {sum}")
    m=m//10
if sum==n:
    print("yes")
else:
    print("no")
