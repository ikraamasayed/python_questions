def isprime(num):
    for i in range (2,num):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    num = 2
    while n:
        if isprime(num):
            yield num 
            n-=1
        num+=1
x = int(input("Enter the no of prime num required"))
it = prime_generator(x)
for e in it:
    print(e,end=" ")
