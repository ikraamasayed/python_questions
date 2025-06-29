# N= int(input("enter the N'th number "))
# sum=0
# start = 9
# d = int(input("enter the difference you want to be in "))
# for i in range (1,N+1):
#     sum=sum+start # 0+9 = 9+13 = 22+17 = 39+21 = 60+25 =85
#     print(f"{sum}+{start}")
#     start+=d # 9+4= 13+4= 17+4 = 21+4
# print("sum of series : ",sum)


# # X^1 + X^2 + X^3 + X^4 + X^5 = sum 
# N=int(input("enter Nth "))
# X= int(input("enter X: "))

# sum =0
# for i in range (1,N+1):
#     sum = sum + X**i
#     # print(sum, X**i)
# print("sum of series : ",sum)


# 9!/x + 13!/x + 17!/x .... N
import math as m
N= int(input("enter the nth"))
X= int(input("enter X: "))
sum=0
a=9

for i in range(1,N+1):
    sum = sum + m.factorial(a)/X
    a+=4
print("sum of series: ",sum)