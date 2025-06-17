a= 12 # global vartable
def W():
    global a # update global variable value 
    a =10 # set to global value
    b= 20
    print(a,b)

W()
print(a)