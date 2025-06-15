numberlist= [12,43,65,87,98,54]
print(max(numberlist))

maximum_no = 0
for m in numberlist:
    if maximum_no < m:
        maximum_no = m
print(maximum_no)