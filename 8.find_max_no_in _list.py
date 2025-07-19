numberlist= [12,43,65,87,98,54]
print(max(numberlist))

maximum = 0
for m in set(numberlist):
    if maximum < m :
        maximum = m 

print(maximum)
