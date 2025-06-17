# Simple factorial using recurrsion logic
def f(n):
    if n == 0: 
        return 1
    else: 
        return n*f(n-1)
    
    # lambda argument : expression
f = lambda n:1 if n ==0 else n*f(n-1)
print(f(8))