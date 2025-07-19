def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
    
def generate_prime(no_of_prime):
    num=2
    while no_of_prime :
        if isprime(num):
            yield num
            no_of_prime-=1
        num+=1

ask_no_of_prime = int(input("enter the no of prime num required: "))
for prime in generate_prime(ask_no_of_prime):
    print(prime,end=" ")
    