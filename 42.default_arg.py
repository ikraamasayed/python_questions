#the arg that are declare and assigned a value while creating a function are called default arg 

def car(name,seats,wheels=4):
    return name,seats,wheels

mercedes = car("MAYBACHH","Black LEATHER")
print(mercedes)