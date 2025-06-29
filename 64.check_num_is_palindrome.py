n = int(input("enter the number"))

original_num = n
reversed_num = 0

while n!=0 :
    digit = n % 10
    print(digit)
    reversed_num = reversed_num * 10 + digit
    n= n // 10
if reversed_num == original_num:
    print("its the palindrom",original_num,reversed_num)  
else: 
    print("its not the palindrom")