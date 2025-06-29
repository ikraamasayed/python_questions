#check if a number is divisible by the sum of its digits

n = 156
m =n
sum = 0
prod = 1
 
while m!= 0:
    d = m%10
    print(d)
    m= m//10
    print(m)
    sum = sum+d

if n%sum ==0:
    print("yes ")
else:
    print("no")