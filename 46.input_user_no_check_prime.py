num = int(input("enter number"))
for i in range(2,num):
    x = num%i
    if x == 0:
        print("number is not prime")
        break
    else:
        print("number is prime")