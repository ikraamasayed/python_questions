#Check the number which is equals to sum of the factorial of digits 
# 145 = 1!+4!+5!
#def factorial(num) is recursive function to calculate factorial of a number


# def factorials(num):
#     if num ==0 or num==1:
#         return 1
#     else : 
#         return num*factorials(num-1)
# n=int(input("enter the number :"))
# total = 0

# numbers= [int(d) for d in str(n)]
# for el in numbers:
#     total+=factorials(el)
# if total==n:
#     print(True)
# else:
#     print(False)


# factorials= [1]
# for i in range(1,10):
#     factorials.append(factorials[-1]*i)
# n = int(input("enter the number : "))
# total=sum(factorials[int(d)]for d in str(n))
# if total == n :
#     print(True)
# else:
#     print(False)

import math
n = int(input("enter the number : "))
total=sum(math.factorial(int(d))for d in str(n))
if total == n :
    print(True)
else:
    print(False)