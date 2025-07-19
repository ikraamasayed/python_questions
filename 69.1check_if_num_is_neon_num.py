# check the number is neon number
# Number, digit of whose sqare is equal to number itself
# Eg: num = 9
# sq = 81
# 8+1 = 9 = num


# def is_neon(number):
#     sq_number= number**2
#     digit = [int(d) for d in str(sq_number)]
#     check_d_total = total(digit)
#     return number == check_d_total

def is_neon(number):
    expression_number = number**2
    while expression_number!=0:
        digit = expression_number%10
        total +=digit
        expression_number= expression_number//10
    return total == number

take_input= int(input("enter the num :"))
if is_neon(take_input):
    print(True)
else:
    print(False)


# other way
num = 9
sq=9**2
print(num == sum([int(el) for el in str(sq)]))