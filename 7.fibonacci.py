fib = [0,1]
n=10 
for i in range (n):
    fib.append(fib[-1]+fib[-2])

print(",".join(str(el)for el in fib))
