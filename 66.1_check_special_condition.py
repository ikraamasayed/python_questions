

# take_input > turn_it_into sum & prod > check if sum of both(sum+prod) == input 


def is_special(number):
    digit = [int(d) for d in str(number) ]
    digit_addition = sum(digit)

    prod = 1
    for d in digit:
        prod *= d
    return digit_addition + prod == number



take_input = int(input("enter the number : "))

if is_special(take_input):
    print(True)
else : 
    print(False)

