#if sum of digit plus producr of digit is equal to the original number


n = int(input("enter the number "))
m=n
sum =0
prod =1
while m!=0:
    d=m%10 
    print(f"d: {d}")
    m=m//10 #
    print(f"m: {m}")
    sum = sum+d
    prod = prod*d
if sum+prod ==n :
    print("yes")
else:
    print("no")