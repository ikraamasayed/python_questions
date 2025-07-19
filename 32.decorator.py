
# decorate that take arguments and key, value pair
def my_decorator(func):
    def wrapper(*args,**kwrgs):
        print('args taken: ',list(args)) # before something
        print('kwrgs taken: ',dict(kwrgs))
        func(*args,**kwrgs) # your function
        print(func.__name__,' decoreated !') # after something
    return wrapper

# -----------------args example---------------------    
@my_decorator
def print_n_time(n):
    # print(f'inside {print_n_time.__name__}')
    print("hello\n"*n)

print_n_time(3)
print()
# ----------------key, value example----------------
@my_decorator
def add(num1=1, num2=2):
    # print('inside ',add.__name__)
    print(num1+num2)

add(num1=2, num2=2)
print()

# --------------no args or kwrgs---------------------

@my_decorator
def print_hello():
    print(f'inside: ',print_hello.__name__)

print_hello()