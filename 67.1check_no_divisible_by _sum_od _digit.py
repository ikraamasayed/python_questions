def check_divisible(number):
    digit = [int(d) for d in str(number)]
    sum_digit = sum(digit)
    return number%sum_digit==0 

take_number = int(input('enter the number : '))
if check_divisible(take_number):
    print(True)
else:
    print(False)