str1= "RaceCar".lower() 
print(str1)
print(str1[::-1]) # [start:stop:steps to take]

if str1 == str1[::-1]:
    print(True)
else:
    print(False)