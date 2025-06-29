n = int(input("Enter the number "))

fact=0
for i in range(1,n+1):
    if(i*(i+1)==n):
        print(f"{i} X {i+1} ={n}")
        fact = i
if fact > 0:
    print("Pronic Number")
else:
    print("Not a Pronic Number")