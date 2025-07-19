"""
take input
find_factor 
    for loop till n number 
        collect factor/divisible num 
check if equals to input 
"""

take_input= int(input("enter the number: "))
sum= 0
for i in range (1,take_input-1):
    if take_input%i==0:
        sum+=i
if sum == take_input:
    print(True)
else:
    print(False)