fib= [0,1]
n=6
for i in range (n):
    fib.append(fib[-1]+fib[-2])
# print(fib)
print(", ".join(str(e) for e in fib))