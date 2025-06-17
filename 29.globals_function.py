#gLobals function returns dictionary
#You can use the globals() function to access or modify global variables
#within a function or code block.

x= 5 
def fun():
    x=10
    d= globals()
    print("local",x,"global",(d['x']))
fun()