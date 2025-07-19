def fibo(n):
    a = 0
    b = 1
    fib_lst =[]
    if n==1:
        print(a)
    else : 
        fib_lst.append(a)
        fib_lst.append(b)
        
        for i in range(n):
            c = a+b
            a = b
            b = c
            fib_lst.append(c)

    print(fib_lst)

fibo(4)