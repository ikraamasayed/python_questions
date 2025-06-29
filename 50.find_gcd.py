num1 = int(input("Enter the number1 :"))
num2 = int(input("Enter the number2 :"))

def gcd(a,b):
    c=a-b
    d=b-a 
    if a==0 or a==b:
        return b
    elif b==0:
        return a
    elif a>b:
        return gcd(c,b)
    return gcd(a,d)

print(gcd (num1,num2))
