# else with loop
i=0 
while i<10 :
    print(i)
    i+=1
else: # finally
    print("out of while in the else ")

for j in range(10,15):
    if j >15:
        break
    print(j)
else: # finally
    print("out of for in else")