# 
take_input= int(input("enter the number: "))
sum= 0
for i in range (1,take_input-1):
    if take_input%i==0:
        sum+=i
if sum > take_input:
    print("Abundant Number")
else:
    print("Deficient Number")